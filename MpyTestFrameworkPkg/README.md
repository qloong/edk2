# Micro-Python Test Framework Package
The Flat Shoal Creek is a project to implement a micro-python based framework and library that provides a set of convenient abstractions designed to remove as much boilerplate as possible from firmware test setup, case development and execution. It aspires to do so in a lightweight and minimalistic fashion. It is general enough to be useful in a variety of firmware testing scenarios. It also a generic testing framework for black box tests, white box tests, functional test, automate UI / human interaction.

## How to build
The Test Framework is dependent on the Micropython for UEFI, so before any further step, please build Micropython for UEFI following 
links from [MicroPythonPkg](http://www.google.com). 

### Get source code

```
git clone the_repo_of_entire_tree
```

### Required Tools
 * Install Maven following offical site tutorial [Installing Apache Maven](https://maven.apache.org/install.html)
 * Install [Python27](https://www.python.org/) to run python tool from source, set environment variable *PYTHON_HOME* as Python27 installation directory
 * Download Chart.bundle.min.js from [ChartJS official site](https://github.com/chartjs/Chart.js/releases) to ```MicroPythonPkg\Report\resources\js```
 * Download jquery-3.3.1.js from  [JQuery official site](https://jquery.com/download/) to ```MicroPythonPkg\Report\resources\js```
 
### Compile
 ```
 python setup.py
 ```
 The executable target will benerated at *the_repo_of_target*

## Setup

It allows the UEFI validator design the test cases and scripts with python language in UEFI environment. The procedure to set up the Flat Shoal Creek Framework is below. 
 * Copy the Flat Shoal Creek Framework into a media disk at root level
 * Create the test scripts under ‘Scripts’ folder.
 * Mount the media disk into the SUT (System Under Test) and boot the SUT into the UEFI shell.
 * Enter the directory of Flat Shoal Creek Framework and use Startup.nsh with parameters to launch it.
 * Some sample test cases are in ‘Scripts’ folder by default. To modify and execute the sample script is a good method to get familiar with this framework and scripts. 
 
 ## Startup.nsh
 The *Startup.nsh* is the user interface to launch the framework, the usage is below:  
 ``` 
 Startup.nsh [-h] [-a [ia32 | x64] [-d] [-t [script name]] [-s [sequence name]] ]
    -h   Help info 
    -a   Load binary for ia32 platform or x64 platform. Besides -h, -a should be first parameter
    -c   Run a Test Case in Script folder
    -s   Run a Test Suite which has a sequence of Test Cases
    -ss  Run a sequences of Test Suite 
   Note: Please specify the platform before other settings
 ```

