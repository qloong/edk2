# Package of MicroPython interpreter for UEFI
This package contains source of the UEFI porting of MicroPython project (https://github.com/micropython).

## Overview
MicroPython for UEFI consists of three parts:
  * A MciroPython driver:

      * The core part of MicroPython interpreter implemented as a protocol.
      * Its source code is in folder MicroPythonDxe.
      * Its binary name is MicroPythonDxe.efi.
  * A MicroPython application:

      * The user interactive interface (wrapper) of MicroPython interpreter, which can launched as a Shell application or a Shell-Independent application (through BDS Boot Option, like an OS loader).
      * Its source code is in folder MicroPythonApp.
      * Its binary name is micropython.efi.
* A virtual console driver:
     * Implement an emulated console device which is used to simulate user interaction, for test purpose.

## Features

#### MicroPython features:

* All official features, except to:
  * Floating point (including math)
  * Inline assembly code
  * Compiled Python bytecode
  * Some hardware feature modules (like pulse, i2c, etc.)
  * Some external libraries (like select, ssl, socket, libffi, etc.)

#### UEFI specific features:

* Asynchronous execution mode (run in the background of UEFI BIOS)
* Full UEFI services support (through uefi module)
* Direct physical memory access (including memory allocation)
* Enhanced regular expression (through _re module)

## How to build

MicroPython for UEFI must be built under edk2 build environment and against the edk2 code base. Currently MicroPython for UEFI can only run and pass the test with binaries built by toolchains VS2013/VS2013x86, VS2015/VS2015x86, and VS2017. Any other toolchains will be supported in the future, if requested.

Building the MicroPython binary for UEFI is the same as building a normal edk2 platform.  Please make sure you have pulled the full tree of edk2 and done a submodule update. For example, build a X64/DEBUG version of executable binaries (suppose the edk2 code base is "C:\edk2"):

    C:\edk2> edksetup.bat
    C:\edk2> build -p MicroPythonPkg\MicroPythonPkg.dsc -a X64 -t VS2017 -b DEBUG

Once the build is completed, there will be three binary files generated under folder <Build>\MicroPythonPkg\DEBUG_VS2017\X64.

- micropython.efi: main application used to launch the MicroPython interpreter
- MicroPythonDxe.efi: a driver which is the actual implementation of MicroPython interpreter and will be loaded automatically by micropython.efi.
- VirtualConsoleDxe.efi: a driver which is used only for interaction of UI test and must be loaded manually in advance.

## Usage

Normally micropython.efi and MicroPythonDxe.efi must be used together and put in the same folder. micropython.efi is used as the entry application for launching MicroPython interpreter in UEFI environment. It always tries to locate and load driver MicroPythonDxe.efi automatically in the same folder as micropython.efi. It's not necessary to load it manually in advance.

Command line options of micropython.efi:

micropython.efi  \[ -a | -c | -i \]  \[<path_to_python_script_file> | "<single_line_python_script>"\]

```shell
-a    Launch the MicroPython interpreter and then exit. Let it run in the background
-c    Execute the Python script passed on command line and then exit
-i    Launch the REPL (after executing the Python script, if given)
```

If no option is specified on command line, the application will simply enter into REPL mode.

## How to access UEFI Services

The UEFI services are provided by module "uefi" (Lib/Uefi/uefi.py). The user must import this module before using any UEFI services in Python script.

This module provides following global types and objects:

- uefi.mem("c_type_string" \[, <memory_address>\] \[, <alloc_page>\] \[, <read_only>\])
  - A Python type used to access physical memory, including a ctypes+struct-like mechanism which can be used to describe the memory type and layout (C data type/structure/function). 
- uefi.efistatus
  - Exception corresponding to error code of EFI_STATUS
- uefi.bs
  - A uefi.mem object used to wrap gBS (EFI_BOOT_SERVICES). Users can use it to access all fields in gBS.
- uefi.rt
  - A uefi.mem object used to wrap gRT (EFI_RUNTIME_SERVICES). Users can use it to access all fields in gRT.
- uefi.ds
  - A uefi.mem object used to wrap gDS (EFI_DXE_SERVICES). Users can use it to access all fields in gDS.
- uefi.st (System Table object)
  - A uefi.mem object used to wrap gST (EFI_SYSTEM_TABLE). Users can use it to access all fields in gST.
- uefi.VariableStorage
  - A Pythonic wrapper of all variable services provided in gRT.

Follow is an example using above UEFI services.

```python
import Lib.Uefi.uefi as uefi

# Reserve 8-byte memory
count = uefi.mem("Q")
try:
    uefi.bs.GetNextMonotonicCount(count.REF())
    print("Next monotoinc number:", count.VALUE)
except efistatus as status:
    print("ERROR: cannot get next monotonic count")

# Access variable "LangCodes"
vars = uefi.VariableStorage("8BE4DF61-93CA-11D2-AA0D-00E098032B8C")
print(vars["LangCodes"])
```

##### Syntax of "c_type_string" in uefi.mem:

Basic data types:

```
'b' : INT8
'B' : UINT8
'h' : INT16
'H' : UINT16
'l' : INT32
'L' : UINT32
'q' : INT64
'Q' : UINT64
'i' : int
'I' : unsigned int
'n' : INTN
'N' : UINTN
'G' : EFI_GUID
'P' : VOID*
'a' : CHAR8[]
'u' : CHAR16[]
'F' : (VOID*)(...)
'E' : EFI_STATUS
'T' : EFI_HANDLE
'O' : <struct>
```

All other complex data types (C structure) must be defined via ucollections.OrderedDict and referenced by form of 'O#<struct_def_variable_name>'. For example, to describe a C structure like below in Python code,

```c
typedef struct {
  EFI_HANDLE  AgentHandle;
  EFI_HANDLE  ControllerHandle;
  UINT32      Attributes;
  UINT32      OpenCount;
} EFI_OPEN_PROTOCOL_INFORMATION_ENTRY;
```

you can do something like,

```python
import uefi
from ucollections import OrderedDict

EFI_OPEN_PROTOCOL_INFORMATION_ENTRY = OrderedDict([
    ("AgentHandle",         "T"),
    ("ControllerHandle",    "T"),
    ("Attributes",          "L"),
    ("OpenCount",           "L"),
])

InfoEntry = uefi.mem("O#EFI_OPEN_PROTOCOL_INFORMATION_ENTRY")
InfoEntry.AgentHandle = uefi.null
InfoEntry.ControllerHandle = 0x12345678 # just for example
InfoEntry.Attributes = 0x80000001
InfoEntry.OpenCount = 0
```

