/** @file

Copyright (c) 2017 - 2018, Intel Corporation. All rights reserved.<BR>
This program and the accompanying materials
are licensed and made available under the terms and conditions of the BSD License
which accompanies this distribution.  The full text of the license may be found at
http://opensource.org/licenses/bsd-license.php

THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.

**/
#include <Library/BaseLib.h>
#include <Library/Debuglib.h>
#include <Library/HobLib.h>
#include <Library/UefiBootServicesTableLib.h>
#include <Library/UefiRuntimeServicesTableLib.h>
#include <Library/MemoryAllocationLib.h>
#include <Library/DxeServicesLib.h>
#include <Library/BaseMemoryLib.h>
#include <Protocol/SimpleFileSystem.h>
#include <Library/PrintLib.h>
#include <Guid/FileSystemInfo.h>
#include <Library/DxeServicesLib.h>
#include "VirtualLogDxe.h"

extern EFI_GUID gEdkiiVirtualLogProtocolGuid;

///
/// EDKII_VIRTUAL_LOG_PROTOCOL
///

EDKII_VIRTUAL_LOG_PROTOCOL mLogInstance = {
  Flush
};

/**
  Load the code coverage data from memory to media disk.

**/
EFI_STATUS
EFIAPI
Flush (
  CONST CHAR16   *FileName,
  CONST CHAR8    *Buffer,
  UINTN           BufferSize,
  CONST CHAR16   *VolumeLabel
  )
{
  EFI_STATUS                          Status;
  EFI_FILE                            *Root;
  EFI_FILE                            *FileHandle;
  UINTN                               BufSize;
  UINTN                               Size;
  UINTN                               HandleNum;
  UINTN                               Index;
  EFI_HANDLE                          *SimpleFsHandle;
  EFI_SIMPLE_FILE_SYSTEM_PROTOCOL     *SimpleFileSystem;
  EFI_FILE_SYSTEM_INFO                *VolumeInfo;
  BOOLEAN                             Found;
  UINT64                              Pos;
  EFI_FILE_INFO *FileInfo;

  Status                        = EFI_SUCCESS;
  Root                          = NULL;
  FileHandle                    = NULL;
  SimpleFsHandle                = NULL;
  Size                          = 0;
  SimpleFileSystem              = NULL;
  Found                         = FALSE;
  FileInfo                      = NULL;

  VolumeInfo = (EFI_FILE_SYSTEM_INFO *)AllocateRuntimeZeroPool(SIZE_OF_EFI_FILE_SYSTEM_INFO + 200);

  if (BufferSize == 0) {
    DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Failed to find a valid log data in memory!!!!!\n"));
    Status = RETURN_BAD_BUFFER_SIZE;
  } else if (VolumeInfo == NULL) {
    DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Failed to allocate VolumeInfo in memory!!!!!\n"));
    Status = RETURN_BAD_BUFFER_SIZE;
  } else {
    Status = gBS->LocateHandleBuffer(
             ByProtocol,
             &gEfiSimpleFileSystemProtocolGuid,
             NULL,
             &HandleNum,
             &SimpleFsHandle
             );
    if (!EFI_ERROR(Status)) {

      for (Index = 0; Index < HandleNum; Index++) {
        Status = gBS->HandleProtocol(
                 SimpleFsHandle[Index],
                 &gEfiSimpleFileSystemProtocolGuid,
                 (VOID **)&SimpleFileSystem
                 );
        if (EFI_ERROR(Status)) {
          if (SimpleFileSystem != NULL) {
            SimpleFileSystem = NULL;
          }
          continue;
        }
        if (SimpleFileSystem == NULL) {
          continue;
        }
        Status = SimpleFileSystem->OpenVolume(SimpleFileSystem, &Root);
        if (EFI_ERROR(Status)) {
          if (SimpleFileSystem != NULL) {
            SimpleFileSystem = NULL;
          }
          if (Root != NULL) {
            Root->Close(Root);
          }
          continue;
        }
        //
        // Get volume information of file system
        //
        Size = SIZE_OF_EFI_FILE_SYSTEM_INFO + 200;
        ZeroMem(VolumeInfo, Size);
        if (Root != NULL) {
          Status      = Root->GetInfo(Root, &gEfiFileSystemInfoGuid, &Size, VolumeInfo);
          if (EFI_ERROR(Status)) {
            if (SimpleFileSystem != NULL) {
              SimpleFileSystem = NULL;
            }
            if (Root != NULL) {
              Root->Close(Root);
            }
            continue;
          }

          if (!StrCmp(VolumeInfo->VolumeLabel, VolumeLabel)) {
            Found = TRUE;
            break;
          }
        }
      }
    }
    if (!Found) {
      DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Failed to find the media disk labelled by %S!!!!!\n", VolumeLabel));
      FreePool(VolumeInfo);
      Status = EFI_ABORTED;
      return Status;
    }
    //
    // Save the log to the file labeld ITSCOV
    //
    if (Root != NULL) {
      Status = Root->Open(Root, &FileHandle, (CHAR16 *)FileName, EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE, 0);
      if (EFI_ERROR(Status)) {
        Status = Root->Open(Root, &FileHandle, (CHAR16 *)FileName, EFI_FILE_MODE_CREATE | EFI_FILE_MODE_READ | EFI_FILE_MODE_WRITE, 0);
      }
      if (EFI_ERROR(Status)) {
        DEBUG((DEBUG_INFO | DEBUG_LOAD, "\nFailed to create file %s.\n", FileName));
        FreePool(VolumeInfo);
        if (Root != NULL) {
          Root->Close(Root);
        }
        return Status;
      }

      BufSize = BufferSize;
      if (FileHandle != NULL) {
        FileInfo = FileHandleGetInfo(FileHandle);
        ASSERT (FileInfo != NULL);
        Pos = FileInfo->FileSize;
        FreePool(FileInfo);

        Status = FileHandle->SetPosition(FileHandle, Pos);
        Status = FileHandle->Write(FileHandle, (UINTN *)&BufferSize, (UINT8 *)Buffer);
        if (EFI_ERROR(Status) || BufferSize != BufSize) {
          DEBUG((DEBUG_INFO | DEBUG_LOAD, "!!!!!Write %s file Failed. Status = %r, BufferSize = %d, CovFileData.Size = %d!!!!!\n", FileName, Status, BufferSize, BufSize));
        } else {
          DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Congratulations! The log %s has been created under the volume %s!!!!!\n", FileName, VolumeLabel));
        }
        if (FileHandle != NULL) {
          FileHandle->Close(FileHandle);
        }
      }

      if (Root != NULL) {
        Root->Close(Root);
      }
    }
  }
  FreePool(VolumeInfo);
  return Status;
}

EFI_STATUS
EFIAPI
LogInit (
  IN EFI_HANDLE           ImageHandle,
  IN EFI_SYSTEM_TABLE     *SystemTable
  )
{
  EFI_STATUS  Status;

  DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Initialize the Virtual log Dxe module!!!!!\n"));

  Status = gBS->InstallProtocolInterface(
           &ImageHandle,
           &gEdkiiVirtualLogProtocolGuid,
           EFI_NATIVE_INTERFACE,
           &mLogInstance
           );

  ASSERT_EFI_ERROR(Status);

  return EFI_SUCCESS;
}

EFI_STATUS
EFIAPI
LogUnload (
  IN EFI_HANDLE           ImageHandle
  )
{
  EFI_STATUS  Status;

  DEBUG((DEBUG_INFO | DEBUG_LOAD, "\n!!!!!Unload the Virtual log Dxe module!!!!!\n"));

  Status = gBS->UninstallProtocolInterface(
           ImageHandle,
           &gEdkiiVirtualLogProtocolGuid,
           &mLogInstance
           );

  ASSERT_EFI_ERROR(Status);

  return EFI_SUCCESS;
}
