# ETS Test & Example: Setup up a boot option which calls upy.efi to launch another test script
import _re as ure
import array
import uefi
import _ets

def input_more(keys):
    for ch in keys:
        _ets.press(ch)
        _ets.suspend(200)

def type_more(key_func, times):
    while times > 0:
        key_func()
        times -= 1

def press_more(key, times, delay=200):
    while times > 0:
        _ets.press(*key)
        _ets.suspend(delay)
        times -= 1

def enter(times=1):
    press_more((0x000D, 0), times, 200)

def esc(times=1):
    press_more((0, 0x0017), times, 200)

def down(times=1):
    press_more((0, 2), times, 200)

def backspace(times=1):
    press_more((8, 0), times, 200)

def delete(times=1):
    press_more((0, 8), times, 200)

def shell(cmd):
    wait_time = 10000
    while (not check(r"Shell>")) and (not check(r"FS[0-9]+:.*\>")):
        _ets.suspend(200)
        wait_time -= 200
        if (wait_time <= 0):
            return
    _ets.suspend(200)
    input_more(cmd)
    enter()

def prompt(text):
    print(">>>", text, "\r\n")
    _ets.suspend(1000)

def goto_menu_option(option):
    prompt("Goto " + "<" + option + ">")
    p = ure.compile(option)
    prev_text, prev_attr = "", []
    while True:
        text,attr=_ets.snapshot()
        if text == prev_text and attr == prev_attr:
            # in case the UI response isn't fast enough
            _ets.suspend(200)
            continue

        index = 0
        while text:
            result = p.split(text)
            if len(result) > 1:
                index += len(result[0])
                if attr[index] == 0x07:
                    return
                text = text[len(result[0])+len(option):]
                index += len(option)
            else:
                break

        prev_text, prev_attr = text, attr
        down()

def enter_menu_option(option):
    goto_menu_option(option)
    enter()

def goto_boot_manager():
    prompt("Goto Boot Manager")
    p = ure.compile("Boot Manager.+")
    while True:
        text,attr=_ets.snapshot()
        result = p.split(text)
        if len(result) == 2:
            index = len(result[0])
            if attr[index] == 0x07:
                break
        down()
    enter()

def goto_menu_app():
    prompt("Goto MenuApp")
    down(5)
    enter()

def return_shell_from_menu_app():
    prompt("Go back to shell")
    esc(2)
    down(2)
    enter(2)

def snapshot():
    screen_text = ""
    screen_attr = []
    for char,attr in _ets.snapshot():
        if char:
            screen_text += chr(char)
        else:
            screen_text += ' '
        screen_attr.append(attr)
    return (screen_text, screen_attr)

    
def check(pattern):
    text, attr = _ets.snapshot()
    lines = text.strip().split('\n')
    for n in range(len(lines)):
        line = lines[0-n-1]
        match = ure.search(pattern, line)
        if match:
            return True
    return False

print("ETS started:\r\n")

