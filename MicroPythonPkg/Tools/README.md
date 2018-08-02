# Tool: genhdr.py
A python script tool used to collect all QSTR references and generate corresponding macro definitions in file qstrdefs.generated.h, as well as to collect version information and generate corresponding macros in file mpversion.h. These two files are needed by MicroPython for build.

## Usage
Note: This tool is only needed to run, if the developer has changed, added new QSTRs and/or upgraded MicroPython, to reflect the correct QDEF() definitions for fixed strings or version strings.

Note: Please initialize Visual Studio build environment before running this tool, which needs compiler to do C file preprocessing.

<Python2/Python3> genhdr.py -a <arch> <path_to_MicroPythonDxe.inf_file>

