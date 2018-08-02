import sys
import uefi
from ucollections import OrderedDict
from unittest import *

class UnicodeStringUnitTest(TestCase):
    def setUp(self):
        log(0, "[Unicode Test: BEGIN]")

    def tearDown(self):
        log(0, "\n[Unicode Test: PASS]")

    def test_double_bytes(self):
        unistr = "\u25ba\u25c4\u25bc\u25b2"
        log(1, "Test string:", "\\u25ba\\u25c4\\u25bc\\u25b2")

        log(2, "unicode(25ba) =", ord(unistr[0]))
        assert(ord(unistr[0]) == 9658)
        log(2, "unicode(25c4) =", ord(unistr[1]))
        assert(ord(unistr[1]) == 9668)
        log(2, "unicode(25bc) =", ord(unistr[2]))
        assert(ord(unistr[2]) == 9660)
        log(2, "unicode(25b2) =", ord(unistr[3]))
        assert(ord(unistr[3]) == 9650)

    def test_mix_bytes(self):
        unistr = "\u25ba0\u25c41\u25bc2\u25b23"
        log(1, "Test string:", "\\u25ba0\\u25c41\\u25bc2\\u25b23")

        log(2, "unicode(25ba) =", ord(unistr[0]))
        assert(ord(unistr[0]) == 9658)

        log(2, "unicode('0') =", ord(unistr[1]))
        assert(ord(unistr[1]) == 48)

        log(2, "unicode(25c4) =", ord(unistr[2]))
        assert(ord(unistr[2]) == 9668)

        log(2, "unicode('1') =", ord(unistr[3]))
        assert(ord(unistr[3]) == 49)

        log(2, "unicode(25bc) =", ord(unistr[4]))
        assert(ord(unistr[4]) == 9660)

        log(2, "unicode('2') =", ord(unistr[5]))
        assert(ord(unistr[5]) == 50)

        log(2, "unicode(25b2) =", ord(unistr[6]))
        assert(ord(unistr[6]) == 9650)

        log(2, "unicode('3') =", ord(unistr[7]))
        assert(ord(unistr[7]) == 51)

    def test_utf8(self):
        unistr = "\u0030123"
        log(1, "Test string:", "\\u0030123")
        log(2, "unicode(30) =",ord(unistr[0]))
        assert(ord(unistr[0]) == 48)
        log(2, "ascii('1') =", ord(unistr[1]))
        assert(ord(unistr[1]) == 49)
        log(2, "ascii('2') =", ord(unistr[2]))
        assert(ord(unistr[2]) == 50)

if __name__ == '__main__':
    mytest = UnicodeStringUnitTest()

