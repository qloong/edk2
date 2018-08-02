/** @file
  Header file for Terminal driver.

Copyright (c) 2006 - 2017, Intel Corporation. All rights reserved.<BR>
Copyright (C) 2016 Silicon Graphics, Inc. All rights reserved.<BR>
This program and the accompanying materials
are licensed and made available under the terms and conditions of the BSD License
which accompanies this distribution.  The full text of the license may be found at
http://opensource.org/licenses/bsd-license.php

THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.

**/

#ifndef _VIRTUAL_LOG_DXE_H_
#define _VIRTUAL_LOG_DXE_H_


#include <Uefi.h>
#include <PiDxe.h>

#include <Guid/GlobalVariable.h>

#include <Protocol/SimpleTextOut.h>
#include <Protocol/DevicePath.h>
#include <Protocol/SimpleTextIn.h>
#include <Protocol/SimpleTextInEx.h>
#include <Protocol/VirtualLog.h>
#include <Guid/ConsoleInDevice.h>
#include <Guid/ConsoleOutDevice.h>
#include <Guid/MdeModuleHii.h>

#include <Library/DebugLib.h>
#include <Library/UefiDriverEntryPoint.h>
#include <Library/UefiLib.h>
#include <Library/BaseMemoryLib.h>
#include <Library/MemoryAllocationLib.h>
#include <Library/UefiBootServicesTableLib.h>
#include <Library/UefiRuntimeServicesTableLib.h>
#include <Library/ReportStatusCodeLib.h>
#include <Library/DevicePathLib.h>
#include <Library/BaseLib.h>
#include <Library/FileHandleLib.h>

/**
  Flush the file context to a media disk labeled VolumeLabel

  @param  FileName                The log file name.
  @param  Buffer                  The context buffer.
  @param  BufferSize              The ascii number in the context buffer.
  @param  VolumeLabel             The volume label.
  
  @retval EFI_SUCCESS              The reset operation succeeds.
  @retval EFI_DEVICE_ERROR         The dependent serial port reset fails.

**/
EFI_STATUS
Flush(
  IN     CONST CHAR16                   *FileName,
  IN     CONST CHAR8                    *Buffer,
  IN     UINTN                          BufferSize,
  IN     CONST CHAR16                  *VolumeLabel
  );

EFI_STATUS
EFIAPI
LogInit (
  IN EFI_HANDLE           ImageHandle,
  IN EFI_SYSTEM_TABLE     *SystemTable
  );

EFI_STATUS
EFIAPI
LogUload (
  IN EFI_HANDLE           ImageHandle
  );
#endif
