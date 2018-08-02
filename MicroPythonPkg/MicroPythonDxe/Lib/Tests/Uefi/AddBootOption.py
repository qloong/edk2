# ETS Test & Example: Setup up a boot option which calls upy.efi to launch another test script
import ets

ets.shell("cls")
ets.shell("exit")
ets.enter_menu_option("Boot Maintenance Manager")
ets.enter_menu_option("Boot Options")
ets.enter_menu_option("Add Boot Option")
ets.enter_menu_option("EFI_EMULATED,")
ets.enter_menu_option("micropython.efi")

# input boot entry name
ets.enter()
ets.input_more("ETS: GetVariable")
ets.enter()

# input boot entry options
ets.down()
ets.enter()
ets.input_more("-a \\\\LABEL:EFI_EMULATED\\Lib\\Tests\\Uefi\\GetVariable.py")
ets.enter()

# save the changes
ets.down()
ets.enter()

# exit to front page
ets.esc(2)
ets.enter_menu_option("Boot Manager")
ets.enter_menu_option("ETS: GetVariable")

