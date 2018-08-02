/**@file

Copyright (c) 2006 - 2016, Intel Corporation. All rights reserved.<BR>
This program and the accompanying materials                          
are licensed and made available under the terms and conditions of the BSD License         
which accompanies this distribution.  The full text of the license may be found at        
http://opensource.org/licenses/bsd-license.php                                            
                                                                                          
THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,                     
WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.             

Module Name:

  ObjuefiTest.c

Abstract:

 

**/


#include <uefi/UefiSpec.h>
#include <stdarg.h>
#include <Library/BaseLib.h>
#include <Library/MemoryAllocationLib.h>
#include <Library/DebugLib.h>




//
// Function Prototypes
//
EFI_STATUS
EFIAPI
ObjuefiTest (
  IN EFI_HANDLE        ImageHandle,
  IN EFI_SYSTEM_TABLE  *SystemTable
  )
;


INT8
ReturnInt8 (INT8 num, ...  )
{
	va_list valist;
	INT8 sum = 0;
	INT8 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, INT8);
	}

	/* clean memory reserved for valist */
    VA_END(valist);

	 return sum;

}


UINT8
ReturnUint8 (UINT8 num, ...  )
{
  va_list valist;
	UINT8 sum = 0;
	UINT8 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, UINT8);
	}

	/* clean memory reserved for valist */
    VA_END(valist);

	 return sum;

}

INT16
ReturnInt16 (INT16 num, ...  )
{
  va_list valist;
  INT16 sum = 0;

  INT16 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
  for (i = 0; i < num; i++) {
    sum += VA_ARG(valist, INT16);
  }

	/* clean memory reserved for valist */
  VA_END(valist);

  return sum;
}


UINT16
ReturnUint16 (UINT16 num, ...  )
{
  va_list valist;
  UINT16 sum = 0;

  UINT16 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
  for (i = 0; i < num; i++) {
    sum += VA_ARG(valist, UINT16);
  }

	/* clean memory reserved for valist */
  VA_END(valist);

  return sum;
}

INT32
ReturnInt32 (INT32 num, ...  )
{
    va_list valist;
	INT32 sum = 0;
	INT32 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, INT32);
	}

	/* clean memory reserved for valist */
    VA_END(valist);

	 return sum;
}

UINT32
ReturnUint32 (UINT32 num, ...  )
{
	va_list valist;
	UINT32 sum = 0;
	UINT32 i;

	/* initialize valist for num number of arguments */
	VA_START(valist, num);

	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
	  sum += VA_ARG(valist, UINT32);
	}

	/* clean memory reserved for valist */
	VA_END(valist);

	return sum;

}

INT64
ReturnInt64 (INT64 num, ...  )
{
  va_list valist;
	INT64 sum = 0;
	INT64 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);

	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, INT64);
	}

	/* clean memory reserved for valist */
  VA_END(valist);
	
	 return sum;
}

UINT64
ReturnUint64 (UINT64 num, ...  )
{
  va_list valist;
	UINT64 sum = 0;
	UINT64 i;

	/* initialize valist for num number of arguments */
	VA_START(valist, num);

	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, UINT64);
	}

	/* clean memory reserved for valist */
  VA_END(valist);

	 return sum;

}

int
ReturnInt (INT8 num, ...  )
{
  va_list valist;
	INT8 sum = 0;
	INT8 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, INT8);
	}

	/* clean memory reserved for valist */
  VA_END(valist);

	 return sum;

}



INT8
ReturnUnsignedInt (INT8 num, ...  )
{
  va_list valist;
	INT8 sum = 0;
	INT8 i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);


	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, INT8);
	}

	/* clean memory reserved for valist */
    VA_END(valist);

	 return sum;

}



INTN
ReturnIntn (INTN num, ...  )
{
  va_list valist;
  INTN sum = 0;
  INTN i;

  /* initialize valist for num number of arguments */
  VA_START(valist, num);


  /* access all the arguments assigned to valist */
  for (i = 0; i < num; i++) {
    sum += VA_ARG(valist, INTN);
  }

  /* clean memory reserved for valist */
  VA_END(valist);
  
  return sum;
}


UINTN
ReturnUintnn (UINTN num, ...  )
{
    va_list valist;
	UINTN sum = 0;
	UINTN i;

	/* initialize valist for num number of arguments */
	 VA_START(valist, num);

	/* access all the arguments assigned to valist */
	for (i = 0; i < num; i++) {
		sum += VA_ARG(valist, UINTN);
	}

	/* clean memory reserved for valist */
    VA_END(valist);

	 return sum;	 
}

void *memset(void *s, int c, size_t n)
{
  unsigned char *d = s;

  while (n--)
    *d++ = (unsigned char)c;

  return s;
}


char *Returnchar8(void)
{
  char *p; 
  char string[100] = "The unexamined life is not worth living";
  p = &string[0];

  return p;
}

CHAR16 *Returnchar16(void)
{  
  static CHAR16 STR[100] = L"The unexamined life is not worth living";
   
  return &STR[0];
}

#pragma pack (1)
struct date
{
   INT64    Year;    // q
   UINT8    Month;   // B
   INT16    Day;     // h
   UINT16   Hour;    // H
   INT32    Minute;  // l
   UINT32   Second;  // L
   UINT64   Nanosecond;  // Q
   INTN	    TimeZone;   // n
 };

 #pragma pack ()

 
 struct date * today; 
 
EFI_STATUS
EFIAPI
ReturnPointer(
  OUT VOID      **Interface
  )
{  
  today = AllocatePool (sizeof(struct date));
  ASSERT (today != NULL);   
  today->Year        = 0x2018;
  today->Month	     = 0x6;
  today->Day         = 0x7;
  today->Hour        = 0x24;
  today->Second      = 0x80000000;
  today->Nanosecond  = 0x7FFFFFFFFFFFFFFF;
  today->TimeZone    = 1;
  
  *Interface = today;	
 
  return EFI_SUCCESS;
}


UINT64
ReturnVariousType (INT8 type, ...  )
{ 
  va_list valist;
  VA_START(valist, type); 
  UINT64 sum;
  
  INT8         b ;
  UINT8        B ; 
  INT16        h ; 
  UINT16       H ; 
  INT32        l ; 
  UINT32       L ; 
  INT64        q ; 
  UINT64       Q ; 
  int          i ;  
  INTN         n ; 
  UINTN		   N ; 
  unsigned int I ; 

  if (type == 1){
    b = VA_ARG(valist, INT8);
    B = VA_ARG(valist, UINT8);
    h = VA_ARG(valist, INT16);
    H = VA_ARG(valist, UINT16);
    l = VA_ARG(valist, INT32);
    L = VA_ARG(valist, UINT32);
    q = VA_ARG(valist, INT64);
    Q = VA_ARG(valist, UINT64);
    i = VA_ARG(valist, int);
	 
    sum = b + B + h + H + l + L + q + Q + i;  
  }

  if (type == 2){
  	N = VA_ARG(valist, UINTN);
	n = VA_ARG(valist, INTN);
    I = VA_ARG(valist, unsigned int);	 
    q = VA_ARG(valist, INT64);
	Q = VA_ARG(valist, UINT64);
	l = VA_ARG(valist, INT32);
	L = VA_ARG(valist, UINT32);
    b = VA_ARG(valist, INT8);
    B = VA_ARG(valist, UINT8);   
	 
    sum = N + n + I+ q + Q +  l  + L+ b + B ;  
  }

  if (type == 3){
    
    B = VA_ARG(valist, UINT8);
	H = VA_ARG(valist, UINT16);
	L = VA_ARG(valist, UINT32);
	Q = VA_ARG(valist, UINT64);
	l = VA_ARG(valist, INT32);
	n = VA_ARG(valist, INTN);
	b = VA_ARG(valist, INT8); 
	q = VA_ARG(valist, INT64);
	i = VA_ARG(valist, int);

	
   sum = b + B + h + H + l + L + q + Q + i;  
  }



  if (type == 4){
  	
    l = VA_ARG(valist, INT32);
    n = VA_ARG(valist, INTN);
    b = VA_ARG(valist, INT8); 
    q = VA_ARG(valist, INT64);
    i = VA_ARG(valist, int);
    B = VA_ARG(valist, UINT8);
    H = VA_ARG(valist, UINT16);
    L = VA_ARG(valist, UINT32);
    Q = VA_ARG(valist, UINT64);
	  
  sum = b + B + h + H + l + L + q + Q + i;  
  }

	if (type == 5){	  

	  L = VA_ARG(valist, UINT32);
	  q = VA_ARG(valist, INT64);
	  Q = VA_ARG(valist, UINT64);
	  i = VA_ARG(valist, int);
	  b = VA_ARG(valist, INT8);
	  B = VA_ARG(valist, UINT8);
	  h = VA_ARG(valist, INT16);
	  H = VA_ARG(valist, UINT16);
	  l = VA_ARG(valist, INT32); 

	sum = b + B + h + H + l + L + q + Q + i;  
	}


	if (type == 6){	  

	  Q = VA_ARG(valist, UINT64);
	  l = VA_ARG(valist, INT32);
	  L = VA_ARG(valist, UINT32);
	  b = VA_ARG(valist, INT8);
	  B = VA_ARG(valist, UINT8); 
	  N = VA_ARG(valist, UINTN);
	  n = VA_ARG(valist, INTN);
	  I = VA_ARG(valist, unsigned int);    
	  q = VA_ARG(valist, INT64);


	 sum = N + n + I+ q + Q +  l  + L+ b + B ;   
	}


	/* clean memory reserved for valist */
  VA_END(valist);

  return sum; 
}



EFI_BOOT_SERVICESS mBootServicess = {

 (MEM_RETURN_INT8)                   ReturnInt8 ,    
 (MEM_RETURN_UINT8)                  ReturnUint8, 
 (MEM_RETURN_INT16)                  ReturnInt16,
 (MEM_RETURN_UINT16)				 ReturnUint16,
 (MEM_RETURN_INT32)                  ReturnInt32,
 (MEM_RETURN_UINT32)                 ReturnUint32,
 (MEM_RETURN_INT64)                  ReturnInt64,
 (MEM_RETURN_UINT64)                 ReturnUint64,
 (MEM_RETURN_INT)                    ReturnInt,
 (MEM_RETURN_UNSIGNED_INT)           ReturnUnsignedInt,
 (MEM_RETURN_INTN)                   ReturnIntn,
 (MEM_RETURN_UINN)                   ReturnUintnn,
 (MEM_RETURN_CHAR8)                  Returnchar8,
 (MEM_RETURN_CHAR16)                 Returnchar16, 
 (MEM_RETURN_PONINTER)               ReturnPointer,
 (MEM_RETURN_VARIOUS_TYPE)           ReturnVariousType,
};



EFI_STATUS
EFIAPI
ObjuefiTest (
  IN EFI_HANDLE        ImageHandle,
  IN EFI_SYSTEM_TABLE  *SystemTable
  )
/*++

 * This  Driver used  to validate objuefi.c 

--*/
{
  SystemTable->BootServicess = &mBootServicess; 
  return EFI_SUCCESS;
}
