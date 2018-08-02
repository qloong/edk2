/** @file
  The Platform Logo Protocol defines the interface to get the Platform logo
  image with the display attribute.

Copyright (c) 2017, Intel Corporation. All rights reserved.<BR>
This program and the accompanying materials are licensed and made available under 
the terms and conditions of the BSD License that accompanies this distribution.  
The full text of the license may be found at
http://opensource.org/licenses/bsd-license.php.                                          
    
THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,                     
WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.

**/

#ifndef __VIRTUAL_LOG_H_
#define __VIRTUAL_LOG_H_

//
// GUID for EDKII Platform Logo Protocol
//
#define EDKII_VIRTUAL_LOG_PROTOCOL_GUID \
  { 0x372f6584, 0xf4c3, 0x47d4, { 0x91, 0x99, 0xac, 0x6c, 0x1b, 0xbe, 0x4e, 0xd } };


typedef struct _EDKII_VIRTUAL_LOG_PROTOCOL EDKII_VIRTUAL_LOG_PROTOCOL;

/**
  Flush the file context to a media disk labeled VolumeLabel

  @param  FileName                The log file name.
  @param  Buffer                  The context buffer.
  @param  BufferSize              The ascii number in the context buffer.
  @param  VolumeLabel             The volume label.
  
  @retval EFI_SUCCESS              The reset operation succeeds.
  @retval EFI_DEVICE_ERROR         The dependent serial port reset fails.

**/
typedef
EFI_STATUS
(EFIAPI *EDKII_VIRTUAL_LOG_FLUSH)(
  IN     CONST CHAR16                         *FileName,
  IN     CONST CHAR8                          *Buffer,
  IN     UINTN                          BufferSize,
  IN     CONST CHAR16                         *VolumeLabel
  );

  struct _EDKII_VIRTUAL_LOG_PROTOCOL {
  EDKII_VIRTUAL_LOG_FLUSH            Flush;
};

extern EFI_GUID gEdkiiVirtualLogProtocolGuid;

#endif
