# ETS Test & Example: Setup up a boot option which calls upy.efi to launch another test script
import ets
import uefi

myets = ets.ets('ets\\log\\testscript.log')

myets.Input('cls' + ets.ENTER)

# Call shell application and verify the output result
myets.Input('Helloworld.efi' + ets.ENTER + ets.ENTER)
myets.FuncKey(ets.ENTER, 4)
result1 = myets.Verify('UEFI Hello World!')
myets.Log ('UEFI Hello World! verify result1 = %s '% str(result1))

# WaitUntil function demo
myets.Input('echo Tiano' + ets.ENTER)
result3= myets.WaitUntil('Tiano', 10)
myets.Log ('Waituntil Tiano string result ' + str(result3))

# Get the color of specified string
precolor, backcolor = myets.GetStrColor ('FS0:\\')
myets.Log ('FS0:\\ precolor, backcolor = %s, %s' + str(precolor), str(backcolor))

precolor, backcolor = myets.GetStrColor ('UEFI')
myets.Log ('UEFI precolor, backcolor = %s, %s' + str(precolor), str(backcolor))

myets.Input('exit' + ets.ENTER)

myets.FuncKey(ets.ESC)


# HII select option
result = myets.SelectOption('Device Manager', ets.LIGHTGRAY + ets.BACKBLACK)
myets.Debug ('result = ' + str(result))
myets.FuncKey(ets.ENTER)

# HII select option
result = myets.SelectOption('Platform Driver Override selection', ets.LIGHTGRAY + ets.BACKBLACK)
myets.Debug ('result = ' + str(result))
myets.FuncKey(ets.ENTER)

# HII select option
result = myets.SelectOption('Only show the PCI')
myets.Debug ('result = ' + str(result))
myets.FuncKey(ets.SPACE+ets.ENTER)
myets.FuncKey(ets.F10)
myets.Input('Y')
myets.FuncKey(ets.ESC, 2)

#myets.Delay(1000)

result = myets.SelectOption('Boot Manager', ets.LIGHTGRAY + ets.BACKBLACK)
myets.Log ('Boot Manager result = ' + str(result), True)

myets.FuncKey(ets.ENTER)

result = myets.SelectOption('UEFI Shell', ets.LIGHTGRAY + ets.BACKBLACK)
myets.Debug ('UEFI Shell result = ' + str(result))


myets.FuncKey(ets.ENTER)
myets.FuncKey(ets.ESC)

# call uefi protocol to get variable
varguid = "8be4df61-93ca-11d2-aa0d-00e098032b8c"
vars = uefi.VariableStorage()

myets.Debug("Timeout =" + str(vars["Timeout", varguid]) + '\r\n')
myets.Debug("ConIn =" + str(vars["ConIn", varguid]) + '\r\n')

myets.Log("Timeout =" + str(vars["Timeout", varguid]) + '\r\n')
myets.Log("ConIn =" + str(vars["ConIn", varguid]) + '\r\n', True)

myets.Input('fs0:' + ets.ENTER)
myets.Input('cd ETS' + ets.ENTER)
myets.Input('ETS.nsh' + ets.ENTER)
