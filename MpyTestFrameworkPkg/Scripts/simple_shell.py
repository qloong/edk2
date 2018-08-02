# # @file
# This file is a demo script to automate shell operations
#
# INTEL CONFIDENTIAL
# Copyright (c) 2017-2018, Intel Corporation. All rights reserved.<BR>
#
# The source code contained or described herein and all documents
# related to the source code ("Material") are owned by Intel Corporation
# or its suppliers or licensors. Title to the Material remains with Intel
# Corporation or its suppliers and licensors. The Material contains trade
# secrets and proprietary and confidential information of Intel or its
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

#Sample case for shell basic command test

import sys
import ure
import mptf

def run(log_path):
    obj = mptf.mptf(log_path)
    obj.Input('cls' + mptf.ENTER)
    obj.Input('fs0:' + mptf.ENTER)
    obj.SetTickTock(200)

    ########   ls   ########
    obj.Info('Shell Command \'ls\': ',True)
    obj.Input('ls')
    obj.FuncKey(mptf.ENTER)
    if obj.WaitUntil('Dir', 10):
        obj.Pass('PASS',True)
    else:
        obj.Fail('FAIL',True)

    ########  echo  ########
    obj.Info('Shell Command \'echo\': ',True)
    obj.Input('cls' + mptf.ENTER)
    obj.Input('echo hello world' + mptf.ENTER)
    if obj.Verify('hello world', None, 2):
        obj.Pass('PASS',True)
    else:
        obj.Fail('FAIL',True)

    ########  exit  ########
    obj.Info('Shell Command \'exit\': ',True)
    obj.Input('exit' + mptf.ENTER)

    result = obj.SelectOption('UEFI Shell', mptf.LIGHTGRAY + mptf.BACKBLACK)
    obj.Debug ('UEFI Shell result = ' + str(result))

    obj.FuncKey(mptf.ENTER)
    obj.FuncKey(mptf.ESC)

    obj.Info('The sample case is end.', True)
    obj.Close()
