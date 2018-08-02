# guid: 8be4df61-93ca-11d2-aa0d00e098032b8c
import uefi
import _ets
import ets

# make sure it's in shell
ets.esc(4)
ets.enter_menu_option("Continue")
ets.enter()

varguid = uefi.guid("8be4df61-93ca-11d2-aa0d-00e098032b8c")
print("GUID =", varguid, '\r\n')
print(str(varguid), '\r\n')
print(len(varguid), '\r\n')

ets.shell("cls")
ets.shell("exit")
# make sure it's at the top level menu
ets.esc(4)
ets.enter_menu_option("Boot Manager")
#goto_menu_app()
ets.enter_menu_option("UEFI BootManagerMenuApp")

VarStore = uefi.VariableStorage("8be4df61-93ca-11d2-aa0d-00e098032b8c")
print("Timeout =", VarStore["Timeout"], '\r\n')
print("ConIn =", VarStore["ConIn"], '\r\n')


print(varguid, '\r\n')
print(hex(varguid.ADDR), '\r\n')

_ets.suspend(500)
guida=uefi.guid("8be4df61-93ca-11d2-aa0d-00e098032b8c")
guidb=uefi.guid("8be4df66-93ca-11d2-aa0d-00e098032b8c")
print(guidb==guida, '\r')
print(varguid==guida, '\r')

_ets.suspend(500)
p = uefi.mem(guida.SIZE, guida.ADDR)
p[0] = 0x66
print(guida, '\r')
print(p.ADDR, '\r')
print(guida==guidb, '\r')

ets.return_shell_from_menu_app()

wrong_types = "wrong types"
ets.input_more(wrong_types)
ets.backspace(len(wrong_types))
ets.shell("fs0:")

print("[TEST DONE]")


