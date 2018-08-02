# Micro-Python Test Framework Package
The project to implement a micro-python based framework and library that provides a set of convenient abstractions designed to remove as much boilerplate as possible from firmware test setup, case development and execution. It aspires to do so in a lightweight and minimalistic fashion. It is general enough to be useful in a variety of firmware testing scenarios. It also a generic testing framework for black box tests, white box tests, functional test, automate UI / human interaction.

## How to build
The Test Framework is dependent on the Micropython for UEFI, so before any further step, please build Micropython for UEFI following 
links from [MicroPythonPkg](http://www.google.com). 

### Get source code

```
git clone the_repo_of_entire_tree\\SHWDEOPENPSI071\Users\yujunma\Desktop\2018_kickoff\ETS\git\ets-poc\MicroPythonPkg
```

### Required Tools
 * Install [Python27](https://www.python.org/) to run python tool from source, set environment variable *PYTHON_HOME* as Python27 installation directory
 * Install Maven following offical site tutorial [Installing Apache Maven](https://maven.apache.org/install.html)
 * Download Chart.bundle.min.js from [ChartJS official site](https://github.com/chartjs/Chart.js/releases) to ```MpyTestFrameworkPkg\Report\resources\js```
 * Download jquery-3.3.1.js from  [JQuery official site](https://jquery.com/download/) to ```MpyTestFrameworkPkg\Report\resources\js```
 
### Compile
 ```
 python setup.py
 ```
 The executable target will generated at *the_repo_of_target*

## Setup 

It allows the UEFI validator design the test cases and scripts with python language in UEFI environment. The procedure to set up the Micro-Python Test Framework is below. 
 * Copy the Flat Shoal Creek Framework into a media disk at root level
 * Create the test scripts under `Scripts` folder.
 * Mount the media disk into the SUT (System Under Test) and boot the SUT into the UEFI shell.
 * Rename the lable of midia disk to "MPTF", the method is 
 ```
    vol -n MPTF
 ```
 * Enter the directory of Micro-Python Test Framework and use Startup.nsh with parameters to launch it. 
  
 ### File structure
 Under the directory of Micro-Python Test Framework, there are several sub-folders and files.
 * Bin
`Bin` folder provides interface to enter python enviroment from shell which does not need to modify. there are two sub-folders corresponding to two kinds of platforms X64 and IA32, respectively.
* Config
Under `Config` folder, there two json format files which can determine suquence of test case including running order and runnning times. For the test case, we have three kinds of concept: case, suite and suites. Case represents the independent sripts under Sripts folder which mentioned later.
Suite is a sequence of cases which can be defined through Test_Suite.json file. Similarly, Suites is a sequence of suite which can be defined through Test_Suites.json file.
* Doc
`Doc` folder contains the script user guide shows all function usage.
* Lib
`Lib` folder contains some libraries which this framework depends on.
* Log
`Log` folder contains the log files after running test case, suite or suites.
* Tools
`Tools` folder provides a tool which can generate the human friendly html report. The usage is
``` 
    java -jar ReportGenerator-1.0-SNAPSHOT-jar-with-dependencies.jar
```
* Report
`Report` contains the html report after the tool under `Tools` runs.
* Scripts
Some sample test cases are in `Scripts` folder by default. What'more, all the test cases created need to be put under this folder. To modify and execute the sample script is a good method to get familiar with this framework and scripts.
* Startup.nsh
 The `Startup.nsh` is the user interface to launch the framework, the usage is below:  
 ```
    Startup.nsh [-h] [-a [ia32 | x64] [-d] [-t [script name]] [-s [sequence name]] ]
        -h   Help info 
        -a   Load binary for ia32 platform or x64 platform. Besides -h, -a should be first parameter
        -c   Run a Test Case in Script folder
        -s   Run a Test Suite which has a sequence of Test Cases
        -ss  Run a sequences of Test Suite 
        Note: Please specify the platform before other settings
 ```
 ### Get Started on Nt32
 * Please Build Nt32 following links from [EDK II](https://github.com/tianocore/tianocore.githubio/wiki/Getting-Started-with-EDK-II) to generate `SecMain.exe`.

 * Copy `%WORKSPACE%\Build\MpyTest` to the same directory as `SecMain.exe`.
 * Double click `SecMain.exe` to run Nt32.
 * After enter shell enviroment, type command below to change volumn lable. 
 ```
     FS0:
     Vol -n MPTF
 ```
 * Enter to `MpyTest` directory to run the test case provided  by default. Use command below to run test case, suite or suites.
      * Run the test case `nt32_shell_hii.py` alone:
     ```
      startup.nsh -a ia32 -c nt32_shell_hii.py
     ```
      * Run the test suite `nt32_test_cases` which is define in `Test_Suite.json` under `Config` folder:
     ```
      startup.nsh -a ia32 -s nt32_test_cases
     ```
      * Run the test suites `nt32_related_suites` which is define in `Test_Suites.json` under `Config` folder:
     ```
      startup.nsh -a ia32 -ss nt32_related_suites
     ```
 * Check the log and generate html report. The log will be put under `Log` folder automaticlly, change to `Tools` folder and use command below to generate html report.
 ```
       java -jar ReportGenerator-1.0-SNAPSHOT-jar-with-dependencies.jar
 ```
 * Change to `Report` folder to check the report generated.
