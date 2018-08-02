# # @file
# This file is a demo script to automate operations both in shell and HII environment
#
# INTEL CONFIDENTIAL
# Copyright (c) 2017-2018, Intel Corporation. All rights reserved.<BR>
#
# The source code contained or described herein and all documents
# related to the source code ("Material") are owned by Intel Corporation
# or its suppliers or licensors. Title to the Material remains with Intel
# Corporation or its suppliers and licensors. The Material contains trade
# secrmptf and proprietary and confidential information of Intel or its
# suppliers and licensors. The Material is protected by worldwide copyright
# and trade secret laws and treaty provisions. No part of the Material may be
# used, copied, reproduced, modified, published, uploaded, posted, transmitted,
# distributed, or disclosed in any way without Intel's prior express written
# permission.
#
# No license under any patent, copyright, trade secret or other intellectual
# property right is granted to or conferred upon you by disclosure or
# delivery of the Materials, either expressly, by implication, inducement,
# estoppel or otherwise. Any license under such intellectual property
# rights must be express and approved by Intel in writing.
#

# mptf Test & Example: Setup up a boot option which calls upy.efi to launch another test script

import sys
import ure
import mptf
import uefi

def run(log_path):
    obj = mptf.mptf(log_path)
    obj.Input('cls' + mptf.ENTER)
    obj.SetTickTock(500)

    # Call shell application and verify the output result
    obj.Input('Helloworld.efi' + mptf.ENTER + mptf.ENTER)
    obj.FuncKey(mptf.ENTER, 4)
    result1 = obj.Verify('UEFI Hello World!')
    if result1 == True:
        obj.Pass('UEFI Hello World! is found')
    else:
        obj.Fail('Fail to find UEFI Hello World!')

    # WaitUntil function demo
    obj.Input('echo Tiano' + mptf.ENTER)
    result3= obj.WaitUntil('Tiano', 10)
    if result3 == True:
        obj.Pass('Tiano is found')
    else:
        obj.Fail('Fail to find Tiano')

    # Get the color of specified string
    fs0_color_list = obj.GmptftrColor ('FS0:\\\\')
    obj.Info('All color occurances of FS0: are:')
    obj.Info(fs0_color_list)

    uefi_color_list = obj.GmptftrColor ('UEFI')
    obj.Info('All color occurances of UEFI are:')
    obj.Info(uefi_color_list)

    obj.Input('exit' + mptf.ENTER)

    obj.FuncKey(mptf.ESC)


    # HII select option
    obj.Info(obj.GmptftrColor('Device Manager'), True)
    result = obj.SelectOption('Device Manager', mptf.LIGHTGRAY + mptf.BACKBLACK)
    obj.Debug ('result = ' + str(result), True)
    obj.FuncKey(mptf.ENTER)

    # HII select option
    result = obj.SelectOption('Platform Driver Override selection', mptf.LIGHTGRAY + mptf.BACKBLACK)
    obj.Debug ('result = ' + str(result))
    obj.FuncKey(mptf.ENTER)

    # HII select option
    result = obj.SelectOption('Only show the PCI')
    obj.Debug ('result = ' + str(result))
    obj.FuncKey(mptf.SPACE+mptf.ENTER)
    obj.FuncKey(mptf.F10)
    obj.Input('Y')
    obj.FuncKey(mptf.ESC, 2)

    #obj.Delay(1000)

    result = obj.SelectOption('Boot Manager', mptf.LIGHTGRAY + mptf.BACKBLACK)
    obj.Info('Boot Manager result = ' + str(result), True)

    obj.FuncKey(mptf.ENTER)

    result = obj.SelectOption('UEFI Shell', mptf.LIGHTGRAY + mptf.BACKBLACK)
    obj.Debug ('UEFI Shell result = ' + str(result))


    obj.FuncKey(mptf.ENTER)
    obj.FuncKey(mptf.ESC)

    # Close the script securely
    obj.Close()
