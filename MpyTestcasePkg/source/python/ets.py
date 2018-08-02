import ure
import array
import uefi
import _ets
#from pip._vendor.pkg_resources import null_ns_handler

#
# Color definition
#
BLACK = 'ETS_FRE_GROUND_COLOR_BLACK'
BLUE = 'ETS_FRE_GROUND_COLOR_BLUE'
GREEN = 'ETS_FRE_GROUND_COLOR_GREEN'
CYAN = 'ETS_FRE_GROUND_COLOR_CYAN'
RED = 'ETS_FRE_GROUND_COLOR_RED'
MAGENTA = 'ETS_FRE_GROUND_COLOR_MAGENTA'
BROWN = 'ETS_FRE_GROUND_COLOR_BROWN'
LIGHTGRAY = 'ETS_FRE_GROUND_COLOR_LIGHTGRAY'
BRIGHT = 'ETS_FRE_GROUND_COLOR_BRIGHT'
DARKGRAY = 'ETS_FRE_GROUND_COLOR_DARKGRAY'
LIGHTBLUE = 'ETS_FRE_GROUND_COLOR_LIGHTBLUE'
LIGHTGREEN = 'ETS_FRE_GROUND_COLOR_LIGHTGREEN'
LIGHTCYAN = 'ETS_FRE_GROUND_COLOR_LIGHTCYAN'
LIGHTRED = 'ETS_FRE_GROUND_COLOR_LIGHTRED'
LIGHTMAGENTA = 'ETS_FRE_GROUND_COLOR_LIGHTMAGENTA'
YELLOW = 'ETS_FRE_GROUND_COLOR_YELLOW'
WHITE = 'ETS_FRE_GROUND_COLOR_WHITE'

BACKBLACK = 'ETS_BACK_GROUND_COLOR_BACKBLACK'
BACKBLUE = 'ETS_BACK_GROUND_COLOR_BACKBLUE'
BACKGREEN = 'ETS_BACK_GROUND_COLOR_BACKGREEN'
BACKCYAN = 'ETS_BACK_GROUND_COLOR_BACKCYAN'
BACKRED = 'ETS_BACK_GROUND_COLOR_BACKRED'
BACKMAGENTA = 'ETS_BACK_GROUND_COLOR_BACKMAGENTA'
BACKBROWN = 'ETS_BACK_GROUND_COLOR_BACKBROWN'
BACKLIGHTGRAY = 'ETS_BACK_GROUND_COLOR_LIGHTGRAY'

#
# EFI Console Colours
#
EFI_BLACK            =     0x00
EFI_BLUE             =     0x01
EFI_GREEN            =     0x02
EFI_CYAN             =     (EFI_BLUE | EFI_GREEN)
EFI_RED              =     0x04
EFI_MAGENTA          =     (EFI_BLUE | EFI_RED)
EFI_BROWN            =     (EFI_GREEN | EFI_RED)
EFI_LIGHTGRAY        =     (EFI_BLUE | EFI_GREEN | EFI_RED)
EFI_BRIGHT           =     0x08
EFI_DARKGRAY         =     (EFI_BLACK | EFI_BRIGHT)
EFI_LIGHTBLUE        =     (EFI_BLUE | EFI_BRIGHT)
EFI_LIGHTGREEN       =     (EFI_GREEN | EFI_BRIGHT)
EFI_LIGHTCYAN        =     (EFI_CYAN | EFI_BRIGHT)
EFI_LIGHTRED         =     (EFI_RED | EFI_BRIGHT)
EFI_LIGHTMAGENTA     =     (EFI_MAGENTA | EFI_BRIGHT)
EFI_YELLOW           =     (EFI_BROWN | EFI_BRIGHT)
EFI_WHITE            =     (EFI_BLUE | EFI_GREEN | EFI_RED | EFI_BRIGHT)

EFI_BACKGROUND_BLACK     = 0x00
EFI_BACKGROUND_BLUE      = 0x10
EFI_BACKGROUND_GREEN     = 0x20
EFI_BACKGROUND_CYAN      = (EFI_BACKGROUND_BLUE | EFI_BACKGROUND_GREEN)
EFI_BACKGROUND_RED       = 0x40
EFI_BACKGROUND_MAGENTA   = (EFI_BACKGROUND_BLUE | EFI_BACKGROUND_RED)
EFI_BACKGROUND_BROWN     = (EFI_BACKGROUND_GREEN | EFI_BACKGROUND_RED)
EFI_BACKGROUND_LIGHTGRAY = (EFI_BACKGROUND_BLUE | EFI_BACKGROUND_GREEN | EFI_BACKGROUND_RED)

BLACK = 'ETS_FRE_GROUND_COLOR_BLACK'
BLUE = 'ETS_FRE_GROUND_COLOR_BLUE'
GREEN = 'ETS_FRE_GROUND_COLOR_GREEN'
CYAN = 'ETS_FRE_GROUND_COLOR_CYAN'
RED = 'ETS_FRE_GROUND_COLOR_RED'
MAGENTA = 'ETS_FRE_GROUND_COLOR_MAGENTA'
BROWN = 'ETS_FRE_GROUND_COLOR_BROWN'
LIGHTGRAY = 'ETS_FRE_GROUND_COLOR_LIGHTGRAY'
BRIGHT = 'ETS_FRE_GROUND_COLOR_BRIGHT'
DARKGRAY = 'ETS_FRE_GROUND_COLOR_DARKGRAY'
LIGHTBLUE = 'ETS_FRE_GROUND_COLOR_LIGHTBLUE'
LIGHTGREEN = 'ETS_FRE_GROUND_COLOR_LIGHTGREEN'
LIGHTCYAN = 'ETS_FRE_GROUND_COLOR_LIGHTCYAN'
LIGHTRED = 'ETS_FRE_GROUND_COLOR_LIGHTRED'
LIGHTMAGENTA = 'ETS_FRE_GROUND_COLOR_LIGHTMAGENTA'
YELLOW = 'ETS_FRE_GROUND_COLOR_YELLOW'
WHITE = 'ETS_FRE_GROUND_COLOR_WHITE'

BACKBLACK = 'ETS_BACK_GROUND_COLOR_BACKBLACK'
BACKBLUE = 'ETS_BACK_GROUND_COLOR_BACKBLUE'
BACKGREEN = 'ETS_BACK_GROUND_COLOR_BACKGREEN'
BACKCYAN = 'ETS_BACK_GROUND_COLOR_BACKCYAN'
BACKRED = 'ETS_BACK_GROUND_COLOR_BACKRED'
BACKMAGENTA = 'ETS_BACK_GROUND_COLOR_BACKMAGENTA'
BACKBROWN = 'ETS_BACK_GROUND_COLOR_BACKBROWN'
BACKLIGHTGRAY = 'ETS_BACK_GROUND_COLOR_LIGHTGRAY'

ColorMapDict = {
    BLACK:'BLACK',
    BLUE:'BLUE',
    GREEN:'GREEN',
    CYAN:'CYAN',
    RED:'RED',
    MAGENTA:'MAGENTA',
    BROWN:'BROWN',
    LIGHTGRAY:'LIGHTGRAY',
    BRIGHT:'BRIGHT',
    DARKGRAY:'DARKGRAY',
    LIGHTBLUE:'LIGHTBLUE',
    LIGHTGREEN:'LIGHTGREEN',
    LIGHTCYAN:'LIGHTCYAN',
    LIGHTRED:'LIGHTRED',
    LIGHTMAGENTA:'LIGHTMAGENTA',
    YELLOW:'YELLOW',
    WHITE:'WHITE',
    BACKBLACK:'BACKBLACK',
    BACKBLUE:'BACKBLUE',
    BACKGREEN:'BACKGREEN',
    BACKCYAN:'BACKCYAN',
    BACKRED:'BACKRED',
    BACKMAGENTA:'BACKMAGENTA',
    BACKBROWN:'BACKBROWN',
    BACKLIGHTGRAY:'BACKLIGHTGRAY'
    }

ColorDict = {   
    BLACK:EFI_BLACK,
    BLUE:EFI_BLUE,
    GREEN:EFI_GREEN,
    CYAN:EFI_CYAN,
    RED:EFI_RED,
    MAGENTA:EFI_MAGENTA,
    BROWN:EFI_BROWN,
    LIGHTGRAY:EFI_LIGHTGRAY,
    BRIGHT:EFI_BRIGHT,
    DARKGRAY:EFI_DARKGRAY,
    LIGHTBLUE:EFI_LIGHTBLUE,
    LIGHTGREEN:EFI_LIGHTGREEN,
    LIGHTCYAN:EFI_LIGHTCYAN,
    LIGHTRED:EFI_LIGHTRED,
    LIGHTMAGENTA:EFI_LIGHTMAGENTA,
    YELLOW:EFI_YELLOW,
    WHITE:EFI_WHITE,
    BACKBLACK:EFI_BACKGROUND_BLACK,
    BACKBLUE:EFI_BACKGROUND_BLUE,
    BACKGREEN:EFI_BACKGROUND_GREEN,
    BACKCYAN:EFI_BACKGROUND_CYAN,
    BACKRED:EFI_BACKGROUND_RED,
    BACKMAGENTA:EFI_BACKGROUND_MAGENTA,
    BACKBROWN:EFI_BACKGROUND_BROWN,
    BACKLIGHTGRAY:EFI_BACKGROUND_LIGHTGRAY
    }

#
# key definition
#
ENTER = '_ETS_ENTER'
TAB = '_ETS_TAB'
ESC = '_ETS_ESC'
BACKSPACE = '_ETS_BACKSPACE'
DELETE = '_ETS_DELETE'
SPACE = '_ETS_SPACE'
HOME = '_ETS_ENTER'
END = '_ETS_TAB'
LEFT = '_ETS_LEFT'
RIGHT = '_ETS_RIGHT'
DOWN = '_ETS_DOWN'
UP = '_ETS_UP'
PAGE_DOWN = '_ETS_PAGE_DOWN'
PAGE_UP = '_ETS_PAGE_UP'
PRINTSCREEN = '_ETS_PRINTSCREEN'
PAUSE = '_ETS_PAUSE'
ALT = '_ETS_ALT'
CMD = '_ETS_CMD'
CTRL = '_ETS_CTRL'
META = '_ETS_META'
SHIFT = '_ETS_SHIFT'
WIN = '_ETS_WIN'
ALTGR = '_ETS_ALTGR'
CAPS_LOCK = '_ETS_CAPS_LOCK'
SCROLL_LOCK = '_ETS_SCROLL_LOCK'
NUM_LOCK = '_ETS_NUM_LOCK'

F1 = '_ETS_F1'
F2 = '_ETS_F2'
F3 = '_ETS_F3'
F4 = '_ETS_F4'
F5 = '_ETS_F5'
F6 = '_ETS_F6'
F7 = '_ETS_F7'
F8 = '_ETS_F8'
F9 = '_ETS_F9'
F10 = '_ETS_F10'
F11 = '_ETS_F11'
F12 = '_ETS_F12'

#
# Required unicode control chars
#
CHAR_BACKSPACE = 0x0008
CHAR_TAB = 0x0009
CHAR_LINEFEED  =       0x000A
CHAR_CARRIAGE_RETURN = 0x000D

#
# EFI Scan codes
#
SCAN_NULL  =   0x0000
SCAN_UP    =   0x0001
SCAN_DOWN  =   0x0002
SCAN_RIGHT =   0x0003
SCAN_LEFT  =   0x0004
SCAN_HOME    = 0x0005
SCAN_END     = 0x0006
SCAN_INSERT  = 0x0007
SCAN_DELETE  = 0x0008
SCAN_PAGE_UP = 0x0009
SCAN_PAGE_DOWN = 0x000A
SCAN_F1        = 0x000B
SCAN_F2        = 0x000C
SCAN_F3        = 0x000D
SCAN_F4        = 0x000E
SCAN_F5        = 0x000F
SCAN_F6        = 0x0010
SCAN_F7        = 0x0011
SCAN_F8        = 0x0012
SCAN_F9        = 0x0013
SCAN_F10       = 0x0014
SCAN_ESC       = 0x0017
SCAN_F11       =           0x0015
SCAN_F12       =           0x0016
SCAN_PAUSE     =           0x0048
SCAN_F13       =           0x0068
SCAN_F14       =           0x0069
SCAN_F15       =           0x006A
SCAN_F16       =           0x006B
SCAN_F17       =           0x006C
SCAN_F18       =           0x006D
SCAN_F19       =           0x006E
SCAN_F20       =           0x006F
SCAN_F21       =           0x0070
SCAN_F22       =           0x0071
SCAN_F23       =           0x0072
SCAN_F24       =           0x0073
SCAN_MUTE      =           0x007F
SCAN_VOLUME_UP     =       0x0080
SCAN_VOLUME_DOWN   =       0x0081
SCAN_BRIGHTNESS_UP =       0x0100
SCAN_BRIGHTNESS_DOWN=      0x0101
SCAN_SUSPEND        =      0x0102
SCAN_HIBERNATE      =      0x0103
SCAN_TOGGLE_DISPLAY =      0x0104
SCAN_RECOVERY       =      0x0105
SCAN_EJECT          =      0x0106

#
# Any Shift or Toggle State that is valid should have
# high order bit set.
#
# Shift state
#
EFI_SHIFT_STATE_VALID     =0x80000000
EFI_RIGHT_SHIFT_PRESSED   =0x00000001
EFI_LEFT_SHIFT_PRESSED    =0x00000002
EFI_RIGHT_CONTROL_PRESSED =0x00000004
EFI_LEFT_CONTROL_PRESSED  =0x00000008
EFI_RIGHT_ALT_PRESSED     =0x00000010
EFI_LEFT_ALT_PRESSED      =0x00000020
EFI_RIGHT_LOGO_PRESSED    =0x00000040
EFI_LEFT_LOGO_PRESSED     =0x00000080
EFI_MENU_KEY_PRESSED      =0x00000100
EFI_SYS_REQ_PRESSED       =0x00000200

#
# Toggle state
#
EFI_TOGGLE_STATE_VALID    =0x80
EFI_KEY_STATE_EXPOSED     =0x40
EFI_SCROLL_LOCK_ACTIVE    =0x01
EFI_NUM_LOCK_ACTIVE       =0x02
EFI_CAPS_LOCK_ACTIVE      =0x04

KeyShitDict = {
    SHIFT:EFI_LEFT_SHIFT_PRESSED,
    ALT:EFI_LEFT_ALT_PRESSED,
    ALTGR:EFI_RIGHT_ALT_PRESSED,
    WIN:EFI_LEFT_LOGO_PRESSED, 
    CTRL:EFI_LEFT_CONTROL_PRESSED,
    PRINTSCREEN:EFI_SYS_REQ_PRESSED,
    META:EFI_LEFT_LOGO_PRESSED,
    CMD:SCAN_NULL #???
    }

KeyToggleDict = {
    CAPS_LOCK:EFI_CAPS_LOCK_ACTIVE, 
    SCROLL_LOCK:EFI_SCROLL_LOCK_ACTIVE, 
    NUM_LOCK:EFI_NUM_LOCK_ACTIVE,
    }
#
# EFI Scan codes
#

KeyUnicodeCharDict = {
    ENTER:CHAR_CARRIAGE_RETURN,
    TAB:CHAR_TAB,
    BACKSPACE:CHAR_BACKSPACE#,
    #LINEFEED:CHAR_LINEFEED
    }

KeyScanCodeDict = {
    ESC:SCAN_ESC,
    DELETE:SCAN_DELETE,
    SPACE:SCAN_NULL, #???
    HOME:SCAN_HOME,
    END:SCAN_END,
    LEFT:SCAN_LEFT,
    RIGHT:SCAN_RIGHT,
    DOWN:SCAN_DOWN,
    UP:SCAN_UP,
    PAGE_DOWN:SCAN_DOWN,
    PAGE_UP:SCAN_UP,
    PAUSE:SCAN_PAUSE, 
    F1:SCAN_F1,
    F2:SCAN_F2,
    F3:SCAN_F3,
    F4:SCAN_F4,
    F5:SCAN_F5,
    F6:SCAN_F6,
    F7:SCAN_F7,
    F8:SCAN_F8,
    F9:SCAN_F9,
    F10:SCAN_F10,
    F11:SCAN_F11, 
    F12:SCAN_F12
}

class ets(object):
    '''
    classdocs
    '''
    #self.log = None
    #self.logfile = None
    #self.loglevel = None
    #self.apiinterval = 0
    #self.envDict     = None

    def __init__(self, logfile='Ets.log', Label ='ETS', loglevel='debug'):
        '''
        Constructor
        '''
        self.logName = logfile
        self.VolumeLabel = Label
        self.logstr = ''
        
    def GetEnv(self, variableName = None):
        if variableName in self.envDict.keys():
            return self.envDict[variableName]
        else:
            return None
    
    def SetEnv(self, variableName, VariableValue):
        self.envDict[variableName] = VariableValue
        return True

    #
    # FuncKey (ets.ENTER)
    # FuncKey (ets.ENTER, 10)
    # FuncKey (ets.SHIFT+ets.ALT, 10, 0.2)
    #
    def FuncKey (self, funckeystr, times = 1, InputSpeed = 100):
        
        UnicodeChar = 0x0
        Scancode    = 0x0
        KeyShift    = 0x0
        KeyToggle   = 0x0
        
        for key in KeyUnicodeCharDict.keys():
            if key in funckeystr:
                UnicodeChar = KeyUnicodeCharDict[key]
                
        for key in KeyScanCodeDict.keys():
            if key in funckeystr:
                Scancode = KeyScanCodeDict[key]
                
        for key in KeyShitDict.keys():
            if key in funckeystr:
                KeyShift = KeyShitDict[key]
                
        for key in KeyToggleDict.keys():
            if key in funckeystr:
                KeyToggle = KeyToggleDict[key]
        
        key = (UnicodeChar, Scancode, KeyShift, KeyToggle)
        
        if key == (0x0, 0x0, 0x0, 0x0):
            return
        
        while times > 0:
            _ets.press(*key)
            _ets.suspend(InputSpeed)
            times -= 1
            
    #type("some text" + Key.TAB + "more text" + Key.TAB + Key.ENTER) or eqivalent
    #type("some text\tmore text\n") 
    
    def Input(self, keystr, InputSpeed = 100):
        
        index  = 0
        
        while index < len(keystr):
            FuncKey = False
            for key in KeyUnicodeCharDict.keys():
                if keystr[index:].startswith(key):
                    self.FuncKey(key, 1, InputSpeed)
                    index = index + len(key)
                    FuncKey = True
                    
            for key in KeyScanCodeDict.keys():
                if keystr[index:].startswith(key):
                    self.FuncKey(key, 1, InputSpeed)
                    index = index + len(key)
                    FuncKey = True
                    
            for key in KeyShitDict.keys():
                if keystr[index:].startswith(key):
                    self.FuncKey(key, 1, InputSpeed)
                    index = index + len(key)
                    FuncKey = True
                    
            for key in KeyToggleDict.keys():
                if keystr[index:].startswith(key):
                    FuncKey(key, 1, InputSpeed)
                    index = index + len(key)  
                    FuncKey = True
                               
            if not FuncKey:
                _ets.press(keystr[index])
                _ets.suspend(InputSpeed)
                index = index + 1
    
    def GetToggleStatus(self):
        return
    
    def Delay (self, msecond):
        _ets.suspend(msecond)
    #
    # if flush = True, the log will be flushed from memory to filesystem of EDS:\Log\FileName
    #
    def Log(self, string, flush = False):
        self.logstr = self.logstr + string
        if flush:
            if self.logstr != '':
                #print (str(self.logName) + str(self.logstr) + str(self.VolumeLabel))
                _ets.log(str(self.logName), str(self.logstr), str(self.VolumeLabel))
            self.logstr = ''
        return True

    def GetScreenSize (self):
        (x, y) = (80, 25)
        return x, y
    
    def SetScreenSize (self, x, y):
        print ("Set the screen mode as" + x + y)
        return True
    
    def GetScreen(self, history = False):
        if not history:
            text, attr = _ets.snapshot()
        else:
            text, attr = _ets.snapshot()
        return (text, attr)
    
    def GetRowString(self, row):
        return None
    
    def clearScreen(self, history = False):
        return True
## Verify whether a specified string with color appear in the current console or history buffer or not.
#
# @param string:        The string to be searched.
# @param FreBackColor   Foreground Color [|Background Color]: Colors for the selected string name, include 
# Black, Red, Green, Yellow, Blue, Magenta, Cyan, White, 
# BackBlack, BackRed, BackGreen, BackYellow, BackBlue, BackMagenta, BackCyan, BackWhite. No color means every color is ok.
# @param history        If False, only check the current console. Or else, check the history and current console together
#
# @retval True/False
#
    def Verify(self, string, FreBackColor = None, history = False):
        #
        # Read the color value
        #
        colorvalue = 0
        if FreBackColor != None:
            for colorkey in ColorDict.keys():
                if colorkey in FreBackColor:
                    colorvalue = colorvalue + ColorDict[colorkey]
        
        text, attr = _ets.snapshot(history)
        p = ure.compile(string + '.*')

        index = 0
        while text:
            result = p.split(text)
            if len(result) > 1:
                index += len(result[0])
                #_ets.debug("%d,%d  = %s\r\n" % (len(text), len(attr), list(map(hex, attr[index:]))))
                #_ets.debug("%x %x %x %x\r\n" % (index, attr[index], attr[index+1], attr[index+2]))
                #_ets.debug("%s\r\n" % result[0])
                if FreBackColor == None:
                    return True
                if attr[index] == colorvalue:
                    return True
                text = text[len(result[0])+len(string):]
                index += len(string)
            else:
                break
            
        return False
    
    def GetStrColor (self, string, history = False):
        
        FreColor  = None
        BackColor = None
        
        text, attr = _ets.snapshot(history)
        p = ure.compile(string + '.*')

        index = 0
        while text:
            result = p.split(text)
            if len(result) > 1:
                index += len(result[0])
                colorvalue = attr[index]
                break
            else:
                return None, None
                
        for colorkey in ColorDict.keys():
            if ColorDict[colorkey] == (colorvalue & 0xf):
                FreColor = ColorMapDict[colorkey]
                break
        
        for colorkey in ColorDict.keys():
            if ColorDict[colorkey] == (colorvalue & 0xf0):
                if colorkey == BLACK:
                    BackColor = ColorMapDict[BACKBLACK]
                else:
                    BackColor = ColorMapDict[colorkey]
                break
                
        return FreColor, BackColor
                    
    def WaitUntil(self, string, timeOut = 10, FreBackColor = None, history = True):
        time   = 0
        result = False
        while time < timeOut*1000:
            result = self.Verify (string, FreBackColor, history)
            if result:
                return True
            _ets.suspend(100)
            time = time + 100
        return False
    
    def WaitVanish(self, string, timeOut = 10, FreBackColor = None, history = True):
        time   = 0
        result = False
        while time < timeOut*1000:
            result = self.Verify (string, FreBackColor, history)
            if not result:
                return True
            _ets.suspend(100)
            time = time + 100
        return False
        
    ## Find the specified option from EDK2 HII page
    #
    # @param string              The option string 
    # @param operation           The option string, suchs as Key.LEFT, Key.RIGHT, Key.DOWN, Key.UP
    # @param maxNum              The max number of do the operation 
    # @param FreBackColor   Foreground Color [|Background Color]: Colors for the selected string name, include 
    # Black, Red, Green, Yellow, Blue, Magenta, Cyan, White, 
    # BackBlack, BackRed, BackGreen, BackYellow, BackBlue, BackMagenta, BackCyan, BackWhite. No color means every color is ok.
    #
    # @retval True/False
        
    def SelectOption(self, string, FreBackColor = None, operation = DOWN, maxNum = 10):
        #
        # Wait 5 seconds in case the UI response isn't fast enough
        #
        index = 0
        prev_text, prev_attr = "", []
        while index < 5000:
            text,attr=_ets.snapshot()
            if text == prev_text and attr == prev_attr:
                _ets.suspend(100)
                index = index + 100
            else:
                break
        
        index = 0
        while index < maxNum:
            if self.Verify(string, FreBackColor):
                return True
            else:
                self.FuncKey(operation)
            _ets.suspend(200)  
            index = index + 1
              
        return False   

print("Edk2 Test Suit initializing ...:\r\n")