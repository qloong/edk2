import sys
import uefi
from ucollections import OrderedDict
from unittest import *

EFI_GUID = OrderedDict([
    ("Data1", 'L'),
    ("Data2", 'H'),
    ("Data3", 'H'),
    ("Data4", '8B'),
])

TEST_STRUCT64 = OrderedDict([
    ("Int_N",       'N'),           # 00
    ("Int_64",      'q'),           # 08
    ("Int_8",       'b'),           # 10
    ("Int_16",      'H'),           # 11
    ("Int_32",      'l'),           # 13
    ("Ptr",         'P'),           # 17
    ("Bit0",        'N0:1'),        # 1F
    ("Bit1_7",      'N1:7'),        #
    ("Bit8_15",     'N8:8'),        #
    ("Bit16_17",    'N16:2'),       #
    ("Bits_left",   'N18:46'),      #
    ("Int_n",       'n'),           # 27
])                                  # 2F

TEST_STRUCT32 = OrderedDict([
    ("Int_N",       'N'),           # 00
    ("Int_64",      'q'),           # 04
    ("Int_8",       'b'),           # 0C
    ("Int_16",      'H'),           # 0D
    ("Int_32",      'l'),           # 0F
    ("Ptr",         'P'),           # 13
    ("Bit0",        'N0:1'),        # 17
    ("Bit1_7",      'N1:7'),        #
    ("Bit8_15",     'N8:8'),        #
    ("Bit16_17",    'N16:2'),       #
    ("Bits_left",   'N18:14'),      #
    ("Int_n",       'n'),           # 1B
])                                  # 1F

class MemBasicUnitTest(TestCase):
    def setUp(self):
        log(0, "[mem object basic tests: BEGIN]")

    def tearDown(self):
        log(0, "\n[mem object basic tests: PASS]")

    def test_b(self):
        log(1, "\n[%s]" % "b - INT8")

        signed_b = uefi.mem('b')
        log(2, "size =", signed_b.SIZE)
        assert(signed_b.SIZE == 1)

        signed_b.VALUE = 0x11
        log(2, "assign value =", 0x11)
        log(2, "   got value =", signed_b.VALUE)
        assert(signed_b.VALUE == 0x11)

        signed_b.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", signed_b.VALUE)
        assert(signed_b.VALUE == -128)

        signed_b.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", signed_b.VALUE)
        assert(signed_b.VALUE == -16)

        signed_b.VALUE = 0x123
        log(2, "assign value =", hex(0x123))
        log(2, "   got value =", hex(signed_b.VALUE))
        assert(signed_b.VALUE == 0x23)


        log(2, "byte[0] =", hex(signed_b[0]))
        assert(signed_b[0] == 0x23)

        try:
            log(2, "byte[1] =", hex(signed_b[1]))
            assert(False)
        except IndexError:
            log(2, "byte[1] = <IndexError>")

        signed_b.FREE()

    def test_B(self):
        log(1, "\n[%s]" % "B - UINT8")

        unsigned_b = uefi.mem('B')
        log(2, "size =", unsigned_b.SIZE)
        assert(unsigned_b.SIZE == 1)

        unsigned_b.VALUE = 0x11
        log(2, "assign value =", 0x11)
        log(2, "   got value =", unsigned_b.VALUE)
        assert(unsigned_b.VALUE == 0x11)

        unsigned_b.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(unsigned_b.VALUE))
        assert(unsigned_b.VALUE == 0x80)

        unsigned_b.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(unsigned_b.VALUE))
        assert(unsigned_b.VALUE == 0xf0)

        unsigned_b.VALUE = 0x123
        log(2, "assign value =", hex(0x123))
        log(2, "   got value =", hex(unsigned_b.VALUE))
        assert(unsigned_b.VALUE == 0x23)

        log(2, "byte[0] =", hex(unsigned_b[0]))
        assert(unsigned_b[0] == 0x23)

        try:
            log(2, "byte[1] =", hex(unsigned_b[1]))
            assert(False)
        except IndexError:
            log(2, "byte[1] = <IndexError>")

        unsigned_b.FREE()

    def test_h(self):
        log(1, "\n[%s]" % "h - INT16")

        signed_h = uefi.mem('h')
        log(2, "size =", signed_h.SIZE)
        assert(signed_h.SIZE == 2)

        signed_h.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(signed_h.VALUE))
        assert(signed_h.VALUE == 0x11)
        
        signed_h.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(signed_h.VALUE))
        assert(signed_h.VALUE == 0x80)

        signed_h.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", signed_h.VALUE)
        assert(signed_h.VALUE == -0x8000)

        signed_h.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", signed_h.VALUE)
        assert(signed_h.VALUE == -16)

        signed_h.VALUE = 0x1234
        log(2, "assign value =", hex(0x1234))
        log(2, "   got value =", hex(signed_h.VALUE))
        assert(signed_h.VALUE == 0x1234)

        signed_h.VALUE = 0x12345
        log(2, "assign value =", hex(0x12345))
        log(2, "   got value =", hex(signed_h.VALUE))
        assert(signed_h.VALUE == 0x2345)

        log(2, "short[0] =", hex(signed_h[0]))
        assert(signed_h[0] == 0x2345)

        signed_h[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(signed_h.VALUE))
        assert(signed_h.VALUE == 0x1)

        try:
            log(2, "short[1] =", hex(signed_h[1]))
            assert(False)
        except IndexError:
            log(2, "short[1] = <IndexError>")

        signed_h.FREE()

    def test_H(self):
        log(1, "\n[%s]" % "H - UINT16")

        unsigned_h = uefi.mem('H')
        log(2, "size =", unsigned_h.SIZE)
        assert(unsigned_h.SIZE == 2)

        unsigned_h.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x11)
        
        unsigned_h.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x80)

        unsigned_h.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x8000)

        unsigned_h.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0xFFF0)

        unsigned_h.VALUE = 0x1234
        log(2, "assign value =", hex(0x1234))
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x1234)

        unsigned_h.VALUE = 0x12345
        log(2, "assign value =", hex(0x12345))
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x2345)

        log(2, "short[0] =", hex(unsigned_h[0]))
        assert(unsigned_h[0] == 0x2345)

        unsigned_h[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(unsigned_h.VALUE))
        assert(unsigned_h.VALUE == 0x1)

        try:
            log(2, "short[1] =", hex(unsigned_h[1]))
            assert(False)
        except IndexError:
            log(2, "short[1] = <IndexError>")

        unsigned_h.FREE()

    def test_l(self):
        log(1, "\n[%s]" % "l - INT32")

        test_data = uefi.mem('i')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 4)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -16)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x123456789
        log(2, "assign value =", hex(0x123456789))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x23456789)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x23456789)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_L(self):
        log(1, "\n[%s]" % "L - UINT32")

        test_data = uefi.mem('I')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 4)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xFFFFFFF0)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x123456789
        log(2, "assign value =", hex(0x123456789))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x23456789)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x23456789)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()


    def test_i(self):
        log(1, "\n[%s]" % "i - int")

        test_data = uefi.mem('i')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 4)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)
        
        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -16)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x123456789
        log(2, "assign value =", hex(0x123456789))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x23456789)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x23456789)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_I(self):
        log(1, "\n[%s]" % "I - unsigned int")

        test_data = uefi.mem('I')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 4)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)
        
        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xFFFFFFF0)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x123456789
        log(2, "assign value =", hex(0x123456789))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x23456789)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x23456789)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_q(self):
        log(1, "\n[%s]" % "q - INT64")

        test_data = uefi.mem('q')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 8)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -16)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x1234567887654321
        log(2, "assign value =", hex(0x1234567887654321))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1234567887654321)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x1234567887654321)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_Q(self):
        log(1, "\n[%s]" % "Q - UINT64")

        test_data = uefi.mem('Q')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 8)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -8
        log(2, "assign value =", -8)
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xfffffffffffffff8)

        test_data.VALUE = -0x80
        log(2, "assign value =", hex(-0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xffffffffffffff80)

        test_data.VALUE = -0x8000
        log(2, "assign value =", hex(-0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xffffffffffff8000)

        test_data.VALUE = -0x80000000
        log(2, "assign value =", hex(-0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xffffffff80000000)

        test_data.VALUE = -0x800000000000
        log(2, "assign value =", hex(-0x800000000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xffff800000000000)

        test_data.VALUE = -0x8000000000000000
        log(2, "assign value =", hex(-0x8000000000000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000000000000000)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x1234567887654321
        log(2, "assign value =", hex(0x1234567887654321))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1234567887654321)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == 0x1234567887654321)

        # MicroPython integer doesn't support unsigned int from syntax point of view.
        # The maximum unsigned integer is 0x7FFFFFFFFFFFFFFF.
        test_data.VALUE = 0x4765432112345678
        log(2, "assign value =", hex(0x4765432112345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x4765432112345678)

        test_data.VALUE = 0x7FFFFFFFFFFFFFFF
        log(2, "assign value =", hex(0x7FFFFFFFFFFFFFFF))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x7FFFFFFFFFFFFFFF)

        test_data.VALUE = 0x7FFFFFFFFFFFFFFE
        log(2, "assign value =", hex(0x7FFFFFFFFFFFFFFE))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x7FFFFFFFFFFFFFFE)

        test_data.VALUE = 0x8000000000000000
        log(2, "assign value =", hex(0x8000000000000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000000000000000)

        test_data.VALUE = 0xFFFFFFFFFFFFFFFF
        log(2, "assign value =", hex(0xFFFFFFFFFFFFFFFF))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0xFFFFFFFFFFFFFFFF)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_a(self):
        log(1, "\n[%s]" % "S - CHAR8[] - Ascii string")

        test_data = uefi.mem("16a")
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 16)

        # common usage
        value = "A string value"
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")

        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # clear the memory
        test_data.VALUE = '\x00' * 15
        assert(test_data[0] == 0)

        # use sequential
        value = ['A', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 'v', 'a', 'l', 'u', 'e', '\x00']
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")
        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # clear the memory
        test_data.VALUE = '\x00' * 15
        assert(test_data[0] == 0)

        # use array (supports buffer protocol)
        value = bytearray([0x41, 0x20, 0x73, 0x74, 0x72, 0x69, 0x6e, 0x67, 0x20, 0x76, 0x61, 0x6c, 0x75, 0x65, 0])
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")
        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # unicode
        value = "Unicode test\u25ba"
        test_data.VALUE = value
        log(2, "assign value = Unicode test\\u25ba")
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == value)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == ord('U'))
        log(2, "test_data[11] =", hex(test_data[11]))
        assert(test_data[11] == ord('t'))
        log(2, "test_data[12] =", hex(test_data[12]))
        assert(test_data[12] != 0)  # utf8 first byte
        log(2, "test_data[13] =", hex(test_data[13]))
        assert(test_data[13] != 0)  # utf8 second byte
        log(2, "test_data[14] =", hex(test_data[14]))
        assert(test_data[14] != 0)  # utf8 third byte
        # 2-byte utf-16 is encoded in 3-byte utf-8. So the string byte size is 15.
        assert(test_data[15] == 0)

        test_data.FREE()

    def test_u(self):
        log(1, "\n[%s]" % "U - CHAR16[] - Unicode (utf-16) string")

        test_data = uefi.mem("16u")
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 32)

        # common usage
        value = "A string value"
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")

        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # clear the memory
        test_data.VALUE = '\x00' * 15
        assert(test_data[0] == 0)

        # use sequential
        value = ['A', ' ', 's', 't', 'r', 'i', 'n', 'g', ' ', 'v', 'a', 'l', 'u', 'e', '\x00']
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")
        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # clear the memory
        test_data.VALUE = '\x00' * 15
        assert(test_data[0] == 0)

        # use array (supports buffer protocol)
        value = bytearray([0x41, 0, 0x20, 0, 0x73, 0, 0x74, 0, 0x72, 0, 0x69, 0, 0x6e, 0, 0x67, 0, 0x20, 0, 0x76, 0, 0x61, 0, 0x6c, 0, 0x75, 0, 0x65, 0, 0, 0])
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == "A string value")
        log(2, "test_data[0] =", test_data[0])
        assert(test_data[0] == 0x41)
        log(2, "test_data[13] =", test_data[13])
        assert(test_data[13] == 0x65)

        # unicode
        value = "Unicode test\u25ba"
        test_data.VALUE = value
        log(2, "assign value =", value)
        log(2, "   got value =", test_data.VALUE)
        log(2, hex(ord(value[11])), hex(ord(test_data.VALUE[11])))
        log(2, hex(ord(value[12])), hex(ord(test_data.VALUE[12])))
        log(2, hex(ord(value[12])), hex(test_data[12]))
        assert(test_data.VALUE == value)

        log(2, "test_data[0] =", hex(test_data[0]))
        assert(test_data[0] == ord('U'))
        log(2, "test_data[11] =", hex(test_data[11]))
        assert(test_data[11] == ord('t'))
        log(2, "test_data[12] =", hex(test_data[12]))
        assert(test_data[12] == 0x25ba)  # utf-16
        log(2, "test_data[13] =", hex(test_data[13]))
        assert(test_data[13] == 0)

        test_data.FREE()

    def test_E(self):
        log(1, "\n[%s]" % "E - EFI_STATUS")

        test_data = uefi.mem('E')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert (test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':
            assert (test_data.VALUE == 0x80000000)
        else:
            assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(test_data.VALUE)) 
        if uefi.arch == 'IA32':
            assert (test_data.VALUE == 0xfffffff0)
        else:
            assert(test_data.VALUE == 0xfffffffffffffff0)    
			
        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x1234567887654321
        log(2, "assign value =", hex(0x1234567887654321))
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':	        
            assert (test_data.VALUE == 0x87654321)	
        else:
            assert(test_data.VALUE == 0x1234567887654321)

        # RETURN_LOAD_ERROR = 0x8000000000000001 = -0x7FFFFFFFFFFFFFFF
        if uefi.arch == 'IA32':
            test_data.VALUE = 0x80000001
            log(2, "assign value =", hex(0x80000001))
            log(2, "   got value =", hex(test_data.VALUE))      
            assert(test_data.VALUE == 0x80000001)
        else:
            test_data.VALUE = -0x7FFFFFFFFFFFFFFF
            log(2, "assign value =", hex(-0x7FFFFFFFFFFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x8000000000000001)

        # RETURN_INVALID_PARAMETER = 0x8000000000000002 = -0x7FFFFFFFFFFFFFFE
        if uefi.arch == 'IA32':
            test_data.VALUE = 0x80000002
            log(2, "assign value =", hex(0x80000002))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x80000002)
        else:
            test_data.VALUE = -0x7FFFFFFFFFFFFFFE
            log(2, "assign value =", hex(-0x7FFFFFFFFFFFFFFE))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x8000000000000002)

        if uefi.arch == 'IA32':
            test_data.VALUE = -0x6FFFFFFF
            log(2, "assign value =", hex(-0x6FFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))        
            assert(test_data.VALUE == 0x90000001)
        else:
            test_data.VALUE = -0x6FFFFFFFFFFFFFFF
            log(2, "assign value =", hex(-0x6FFFFFFFFFFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x9000000000000001)

        if uefi.arch == 'IA32':
            test_data.VALUE = -0x30000001
            log(2, "assign value =", hex(-0x30000001))
            log(2, "   got value =", hex(test_data.VALUE))        
            assert(test_data.VALUE == 0xcfffffff)
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0xcfffffff)
        else:
            test_data.VALUE = -0x3000000000000001
            log(2, "assign value =", hex(-0x3000000000000001))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0xcfffffffffffffff)

            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0xcfffffffffffffff)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_G(self):
        log(1, "\n[%s]" % "G - EFI_GUID")

        test_data = uefi.mem('G')
        log(2, "size =", test_data.SIZE)
        assert(test_data.SIZE == 16)

        test_value = "8BE4DF61-93CA-11D2-AA0D-00E098032B8C"
        test_guid = uefi.guid(test_value)
        test_data.VALUE = test_value
        log(2, "assign value =", test_value)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == test_value)
        assert(test_data == test_guid)
        
        test_data.CAST("O#EFI_GUID")
        assert(test_data.SIZE == 16)

        log(2, "EFI_GUID.Data1    = %08X" % test_data.Data1)
        assert(test_data.Data1 == 0x8BE4DF61)
        log(2, "EFI_GUID.Data2    = %04X" % test_data.Data2)
        assert(test_data.Data2 == 0x93CA)
        log(2, "EFI_GUID.Data3    = %04X" % test_data.Data3)
        assert(test_data.Data3 == 0x11D2)
        log(2, "EFI_GUID.Data4[0] = %02X" % test_data.Data4[0])
        assert(test_data.Data4[0] == 0xAA)
        log(2, "EFI_GUID.Data4[1] = %02X" % test_data.Data4[1])
        assert(test_data.Data4[1] == 0x0D)
        log(2, "EFI_GUID.Data4[2] = %02X" % test_data.Data4[2])
        assert(test_data.Data4[2] == 0x00)
        log(2, "EFI_GUID.Data4[3] = %02X" % test_data.Data4[3])
        assert(test_data.Data4[3] == 0xE0)
        log(2, "EFI_GUID.Data4[4] = %02X" % test_data.Data4[4])
        assert(test_data.Data4[4] == 0x98)
        log(2, "EFI_GUID.Data4[5] = %02X" % test_data.Data4[5])
        assert(test_data.Data4[5] == 0x03)
        log(2, "EFI_GUID.Data4[6] = %02X" % test_data.Data4[6])
        assert(test_data.Data4[6] == 0x2B)
        log(2, "EFI_GUID.Data4[7] = %02X" % test_data.Data4[7])
        assert(test_data.Data4[7] == 0x8C)

        test_data.CAST('G')
        test_value = "8BE4DF6193CA-11D2-AA0D-00E098032B8C"
        log(2, "assign value =", test_value)
        try:
            test_data.VALUE = test_value
            assert(False)
        except ValueError as Excpt:
            log(2, "   got value =", str(Excpt))
            assert(True)

        test_value = "8BE4DF61-93CA-11D2-AA0D-00E098032B8"
        log(2, "assign value =", test_value)
        try:
            test_data.VALUE = test_value
            assert(False)
        except ValueError as Excpt:
            log(2, "   got value =", str(Excpt))
            assert(True)

        test_value = "8BE4DF61 93CA 11D2 AA0D00E098032B8C"
        log(2, "assign value =", test_value)
        try:
            test_data.VALUE = test_value
            assert(False)
        except ValueError as Excpt:
            log(2, "   got value =", str(Excpt))
            assert(True)

    def test_n(self):
        log(1, "\n[%s]" % "n - INTN")

        test_data = uefi.mem('n')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert(test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':
            assert(test_data.VALUE == -0x80000000)
        else:
            assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", test_data.VALUE)
        assert(test_data.VALUE == -16)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x1234567887654321
        log(2, "assign value =", hex(0x1234567887654321))
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':
            assert(test_data.VALUE == -0x789abcdf)
        else:
            assert(test_data.VALUE == 0x1234567887654321)

        # RETURN_LOAD_ERROR = 0x8000000000000001 = -0x7FFFFFFFFFFFFFFF
        if uefi.arch == 'IA32':
            test_data.VALUE = -0x7FFFFFFF
            log(2, "assign value =", hex(-0x7FFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x7FFFFFFF)
        else:
            test_data.VALUE = -0x7FFFFFFFFFFFFFFF
            log(2, "assign value =", hex(-0x7FFFFFFFFFFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x7FFFFFFFFFFFFFFF)

        # RETURN_INVALID_PARAMETER = 0x8000000000000002 = -0x7FFFFFFFFFFFFFFE
        if uefi.arch == 'IA32':
            test_data.VALUE = -0x7FFFFFFE
            log(2, "assign value =", hex(-0x7FFFFFFE))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x7FFFFFFE)
        else:
            test_data.VALUE = -0x7FFFFFFFFFFFFFFE
            log(2, "assign value =", hex(-0x7FFFFFFFFFFFFFFE))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x7FFFFFFFFFFFFFFE)

        if uefi.arch == 'IA32':
            test_data.VALUE = -0x6FFFFFFF
            log(2, "assign value =", hex(-0x6FFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x6FFFFFFF)
        else:
            test_data.VALUE = -0x6FFFFFFFFFFFFFFF
            log(2, "assign value =", hex(-0x6FFFFFFFFFFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x6FFFFFFFFFFFFFFF)

        if uefi.arch == 'IA32':
            test_data.VALUE = -0x30000001
            log(2, "assign value =", hex(-0x30000001))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x30000001)

            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == -0x30000001)
        else:
            test_data.VALUE = -0x3000000000000001
            log(2, "assign value =", hex(-0x3000000000000001))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == -0x3000000000000001)

            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == -0x3000000000000001)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_N(self):
        log(1, "\n[%s]" % "N - UINTN")

        test_data = uefi.mem('N')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert(test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        test_data.VALUE = 0x11
        log(2, "assign value =", hex(0x11))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x11)

        test_data.VALUE = 0x80
        log(2, "assign value =", hex(0x80))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80)

        test_data.VALUE = 0x8000
        log(2, "assign value =", hex(0x8000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x8000)

        test_data.VALUE = 0x80000000
        log(2, "assign value =", hex(0x80000000))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x80000000)

        test_data.VALUE = -16
        log(2, "assign value =", -16)
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':
            assert(test_data.VALUE == 0xfffffff0)
        else:
            assert(test_data.VALUE == 0xfffffffffffffff0)

        test_data.VALUE = 0x12345678
        log(2, "assign value =", hex(0x12345678))
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x12345678)

        test_data.VALUE = 0x1234567887654321
        log(2, "assign value =", hex(0x1234567887654321))
        log(2, "   got value =", hex(test_data.VALUE))
        if uefi.arch == 'IA32':
            assert(test_data.VALUE == 0x87654321)

            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x87654321)
        else:
            assert(test_data.VALUE == 0x1234567887654321)

            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1234567887654321)

        # MicroPython integer doesn't support unsigned int from syntax point of view.
        # So the maximum unsigned integer is 0x7FFFFFFFFFFFFFFF.
        if uefi.arch == 'IA32':
            test_data.VALUE = 0x4765432112345678
            log(2, "assign value =", hex(0x4765432112345678))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x12345678)
        else:
            test_data.VALUE = 0x4765432112345678
            log(2, "assign value =", hex(0x4765432112345678))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x4765432112345678)

        if uefi.arch == 'IA32':
            test_data.VALUE = 0x7FFFFFFF
            log(2, "assign value =", hex(0x7FFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x7FFFFFFF)
        else:
            test_data.VALUE = 0x7FFFFFFFFFFFFFFF
            log(2, "assign value =", hex(0x7FFFFFFFFFFFFFFF))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x7FFFFFFFFFFFFFFF)

        if uefi.arch == 'IA32':
            test_data.VALUE = 0x7FFFFFFE
            log(2, "assign value =", hex(0x7FFFFFFE))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x7FFFFFFE)
        else:
            test_data.VALUE = 0x7FFFFFFFFFFFFFFE
            log(2, "assign value =", hex(0x7FFFFFFFFFFFFFFE))
            log(2, "   got value =", hex(test_data.VALUE))
            assert(test_data.VALUE == 0x7FFFFFFFFFFFFFFE)

        test_data[:] = [1,2,3,4]
        log(2, "assign value =", [1,2,3,4])
        log(2, "   got value =", hex(test_data.VALUE))
        assert(test_data.VALUE == 0x1)

        try:
            log(2, "test_data[0] =", hex(test_data[0]))
            assert(test_data[0] == 0x1)
            log(2, "test_data[1] =", hex(test_data[1]))
            assert(False)
        except IndexError:
            log(2, "test_data[1] = <IndexError>")

        test_data.FREE()

    def test_P(self):
        log(1, "\n[%s]" % "P - VOID*")

        test_data = uefi.mem('P')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert(test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        # get the address
        log(2, "  &P =", hex(test_data.ADDR))
        # invalid address at this time
        log(2, "   P =", hex(test_data.VALUE))

        # de-reference operation '*'
        # int *p
        p_int = uefi.mem('N')
        p_int.VALUE = 0x12345678
        log(2, "   N =", hex(p_int.VALUE));
        log(2, "  &N =", hex(p_int.ADDR));

        # assgining mem object means assigning its address.
        log(2, " (P <= &N)")
        test_data.VALUE = p_int.ADDR  # equivalent to test_data.VALUE = p_int.ADDR
        log(2, " &PN =", hex(test_data.ADDR))
        log(2, "   P =", hex(test_data.VALUE))
        assert(test_data.VALUE == p_int.ADDR)
        log(2, "  *P =", hex(test_data.DREF("PN").VALUE))
        assert(test_data.DREF("PN").VALUE == p_int.VALUE)

        # get address operation '&'
        pp_int = p_int.REF()
        log(2, " &PN =", hex(pp_int.ADDR));
        log(2, "*&PN =", hex(pp_int.DREF("PN").VALUE));
        assert(pp_int == p_int.ADDR)
        assert(pp_int.VALUE == p_int)
        assert(pp_int.DREF("PN").VALUE == p_int.VALUE)

        p_int.FREE()
        test_data.FREE()

    def test_F(self):
        log(1, "\n[%s]" % "F - (*FUNC)()")

        test_data = uefi.mem('F')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert(test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        addr = 0x12345678
        log(2, "test_data = 0x%x" % addr)
        test_data.VALUE = addr
        assert(test_data == addr)

        test_data.FREE()

    def test_T(self):
        log(1, "\n[%s]" % "T - EFI_HANDLE")

        test_data = uefi.mem('T')
        log(2, "size =", test_data.SIZE)
        if uefi.arch == 'IA32':
            assert(test_data.SIZE == 4)
        else:
            assert(test_data.SIZE == 8)

        addr = 0x12345678
        log(2, "test_data = 0x%x" % addr)
        test_data.VALUE = addr
        assert(test_data == addr)

        test_data.FREE()

    def test_O(self):
        log(1, "\n[%s]" % "O - struct")

        if uefi.arch == 'IA32':
            test_data = uefi.mem('O#TEST_STRUCT32')
            log(2, "size =", test_data.SIZE)
            assert(test_data.SIZE == 0x1F)
        else:
            test_data = uefi.mem('O#TEST_STRUCT64')
            log(2, "size =", test_data.SIZE)
            assert(test_data.SIZE == 0x2F)

        # struct {
        #   UINTN       Int_n;
        #   UINT64      Int_64;
        #   INT8        Int_8;
        #   UINT16      Int_16;
        #   INT32       Int_32;
        #   VOID        *Ptr;
        #   UINTN       Bit0     :1;
        #   UINTN       Bit1_7   :7;
        #   UINTN       Bit8_15  :8;
        #   UINTN       Bit16_17 :2;
        #   UINTN       Bits_left:46;
        #   INTN        Int_n;
        #}

        if uefi.arch == 'IA32':
            data = 0x123456789abcdef0
            test_data.Int_N = data
            log(2, "test_data.Int_N =", hex(test_data.Int_N), "<=", hex(data))
            assert(test_data.Int_N == 0x9abcdef0)
        else:
            data = 0x123456789abcdef0
            test_data.Int_N = data
            log(2, "test_data.Int_N =", hex(test_data.Int_N), "<=", hex(data))
            assert(test_data.Int_N == data)

        data = -0x123456789abcdef0
        test_data.Int_64 = data
        log(2, "test_data.Int_64 =", hex(test_data.Int_64), "<=", hex(data))
        assert(test_data.Int_64 == data)

        data = -31
        test_data.Int_8 = data
        log(2, "test_data.Int_8 =", hex(test_data.Int_8), "<=", hex(data))
        assert(test_data.Int_8 == data)

        data = 0x4fa9
        test_data.Int_16 = data
        log(2, "test_data.Int_16 =", hex(test_data.Int_16), "<=", hex(data))
        assert(test_data.Int_16 == data)

        data = -0x0fedcba9
        test_data.Int_32 = data
        log(2, "test_data.Int_32 =", hex(test_data.Int_32), "<=", hex(data))
        assert(test_data.Int_32 == data)

        test_data.Ptr = 0
        log(2, "test_data.Ptr =", test_data.Ptr)
        assert(test_data.Ptr == 0)

        test_data.Bit0 = 1
        log(2, "test_data.Bit0 =", hex(test_data.Bit0))
        assert(test_data.Bit0 == 1)

        test_data.Bit1_7 = 0x69
        log(2, "test_data.Bit1_7 =", hex(test_data.Bit1_7))
        assert(test_data.Bit1_7 == 0x69)

        test_data.Bit8_15 = 0x96
        log(2, "test_data.Bit8_15 =", hex(test_data.Bit8_15))
        assert(test_data.Bit8_15 == 0x96)

        test_data.Bit16_17 = 0x2
        log(2, "test_data.Bit16_17 =", hex(test_data.Bit16_17))
        assert(test_data.Bit16_17 == 2)

        if uefi.arch == 'IA32':
            test_data.Bits_left = 0x5A5A
            log(2, "test_data.Bits_left =", hex(test_data.Bits_left))
            assert(test_data.Bits_left == 0x5A5A & ((1 << 14) - 1))

            test_data.Int_n = -0x12345678
            log(2, "test_data.Int_n =", hex(test_data.Int_n))
            assert(test_data.Int_n == -0x12345678)
        else:
            test_data.Bits_left = 0x2A5A5A5A5A5A
            log(2, "test_data.Bits_left =", hex(test_data.Bits_left))
            assert(test_data.Bits_left == 0x2A5A5A5A5A5A)

            test_data.Int_n = -0x123456789abcdef0
            log(2, "test_data.Int_n =", hex(test_data.Int_n))
            assert(test_data.Int_n == -0x123456789abcdef0)

        ptr = uefi.mem("%dB" % test_data.SIZE, test_data.ADDR)

        # Int_N
        log(2, "ptr[00] =", hex(ptr[0x00]))
        assert(ptr[0x00] == 0xf0)
        log(2, "ptr[01] =", hex(ptr[0x01]))
        assert(ptr[0x01] == 0xde)
        log(2, "ptr[02] =", hex(ptr[0x02]))
        assert(ptr[0x02] == 0xbc)
        log(2, "ptr[03] =", hex(ptr[0x03]))
        assert(ptr[0x03] == 0x9a)

        if uefi.arch == 'IA32':
            # Int_64
            log(2, "ptr[04] =", hex(ptr[0x04]))
            assert(ptr[0x04] == 0x10)
            log(2, "ptr[05] =", hex(ptr[0x05]))
            assert(ptr[0x05] == 0x21)
            log(2, "ptr[06] =", hex(ptr[0x06]))
            assert(ptr[0x06] == 0x43)
            log(2, "ptr[07] =", hex(ptr[0x07]))
            assert(ptr[0x07] == 0x65)
            log(2, "ptr[08] =", hex(ptr[0x08]))
            assert(ptr[0x08] == 0x87)
            log(2, "ptr[09] =", hex(ptr[0x09]))
            assert(ptr[0x09] == 0xa9)
            log(2, "ptr[0a] =", hex(ptr[0x0a]))
            assert(ptr[0x0a] == 0xcb)
            log(2, "ptr[0b] =", hex(ptr[0x0b]))
            assert(ptr[0x0b] == 0xed)

            # Int_8
            log(2, "ptr[0c] =", hex(ptr[0x0c]))
            assert(ptr[0x0c] == 0xE1)

            # Int_16
            log(2, "ptr[0d] =", hex(ptr[0x0d]))
            assert(ptr[0x0d] == 0xa9)
            log(2, "ptr[0e] =", hex(ptr[0x0e]))
            assert(ptr[0x0e] == 0x4f)

            # Int_32
            log(2, "ptr[0f] =", hex(ptr[0x0f]))
            assert(ptr[0x0f] == 0x57)
            log(2, "ptr[10] =", hex(ptr[0x10]))
            assert(ptr[0x10] == 0x34)
            log(2, "ptr[11] =", hex(ptr[0x11]))
            assert(ptr[0x11] == 0x12)
            log(2, "ptr[12] =", hex(ptr[0x12]))
            assert(ptr[0x12] == 0xf0)

            # Ptr
            log(2, "ptr[13] =", hex(ptr[0x13]))
            assert(ptr[0x13] == 0)
            log(2, "ptr[14] =", hex(ptr[0x14]))
            assert(ptr[0x14] == 0)
            log(2, "ptr[15] =", hex(ptr[0x15]))
            assert(ptr[0x15] == 0)
            log(2, "ptr[16] =", hex(ptr[0x16]))
            assert(ptr[0x16] == 0)

            # Bit0-63 = 0xA9 69 69 69 69 6A 96 D3
            log(2, "ptr[17] =", hex(ptr[0x17]))
            assert(ptr[0x17] == 0xd3)
            log(2, "ptr[18] =", hex(ptr[0x18]))
            assert(ptr[0x18] == 0x96)
            log(2, "ptr[19] =", hex(ptr[0x19]))
            assert(ptr[0x19] == 0x6a)
            log(2, "ptr[1a] =", hex(ptr[0x1a]))
            assert(ptr[0x1a] == 0x69)

            # Int_n
            log(2, "ptr[1b] =", hex(ptr[0x1b]))
            assert(ptr[0x1b] == 0x88)
            log(2, "ptr[1c] =", hex(ptr[0x1c]))
            assert(ptr[0x1c] == 0xa9)
            log(2, "ptr[1d] =", hex(ptr[0x1d]))
            assert(ptr[0x1d] == 0xcb)
            log(2, "ptr[1e] =", hex(ptr[0x1e]))
            assert(ptr[0x1e] == 0xed)

            # Update some fields through struct field way and memory way
            log(2, "\n<Field update test>")
            test_data.Int_8 = 31
            log(2, "test_data.Int_8 <=", hex(test_data.Int_8))
            assert(test_data.Int_8 == 31)
            log(2, "ptr[0b] =", hex(ptr[0x0b]))
            assert(ptr[0x0b] == 0xed)
            log(2, "ptr[0c] =", hex(ptr[0x0c]))
            assert(ptr[0x0c] == 31)
            log(2, "ptr[0d] =", hex(ptr[0x0d]))
            assert(ptr[0x0d] == 0xa9)

            test_data.Int_32 = 0x0fedcba9
            log(2, "test_data.Int_32 <=", hex(test_data.Int_32))
            assert(test_data.Int_32 == 0x0fedcba9)

            log(2, "ptr[0e] =", hex(ptr[0x0e])) # check if it will cross the field border or not
            assert(ptr[0x0e] == 0x4f)
            log(2, "ptr[0f] =", hex(ptr[0x0f]))
            assert(ptr[0x0f] == 0xa9)
            log(2, "ptr[10] =", hex(ptr[0x10]))
            assert(ptr[0x10] == 0xcb)
            log(2, "ptr[11] =", hex(ptr[0x11]))
            assert(ptr[0x11] == 0xed)
            log(2, "ptr[12] =", hex(ptr[0x12]))
            assert(ptr[0x12] == 0x0f)
            log(2, "ptr[13] =", hex(ptr[0x13])) # check if it will cross the field border or not
            assert(ptr[0x13] == 0)

            test_data.Bit1_7 = 0x6e
            log(2, "test_data.Bit1_7 <=", hex(test_data.Bit1_7))
            assert(test_data.Bit1_7 == 0x6e)
            log(2, "test_data.Bit0 =", hex(test_data.Bit0))
            assert(test_data.Bit0 == 1)
            log(2, "test_data.Bit8_15 =", hex(test_data.Bit8_15))
            assert(test_data.Bit8_15 == 0x96)
            log(2, "ptr[17] =", hex(ptr[0x17]))
            assert(ptr[0x17] == 0xdd)
            log(2, "ptr[18] =", hex(ptr[0x18]))
            assert(ptr[0x18] == 0x96)
        else:
            log(2, "ptr[04] =", hex(ptr[0x04]))
            assert(ptr[0x04] == 0x78)
            log(2, "ptr[05] =", hex(ptr[0x05]))
            assert(ptr[0x05] == 0x56)
            log(2, "ptr[06] =", hex(ptr[0x06]))
            assert(ptr[0x06] == 0x34)
            log(2, "ptr[07] =", hex(ptr[0x07]))
            assert(ptr[0x07] == 0x12)

            # Int_64
            log(2, "ptr[08] =", hex(ptr[0x08]))
            assert(ptr[0x08] == 0x10)
            log(2, "ptr[09] =", hex(ptr[0x09]))
            assert(ptr[0x09] == 0x21)
            log(2, "ptr[0a] =", hex(ptr[0x0a]))
            assert(ptr[0x0a] == 0x43)
            log(2, "ptr[0b] =", hex(ptr[0x0b]))
            assert(ptr[0x0b] == 0x65)
            log(2, "ptr[0c] =", hex(ptr[0x0c]))
            assert(ptr[0x0c] == 0x87)
            log(2, "ptr[0d] =", hex(ptr[0x0d]))
            assert(ptr[0x0d] == 0xa9)
            log(2, "ptr[0e] =", hex(ptr[0x0e]))
            assert(ptr[0x0e] == 0xcb)
            log(2, "ptr[0f] =", hex(ptr[0x0f]))
            assert(ptr[0x0f] == 0xed)

            # Int_8
            log(2, "ptr[10] =", hex(ptr[0x10]))
            assert(ptr[0x10] == 0xE1)

            # Int_16
            log(2, "ptr[11] =", hex(ptr[0x11]))
            assert(ptr[0x11] == 0xa9)
            log(2, "ptr[12] =", hex(ptr[0x12]))
            assert(ptr[0x12] == 0x4f)

            # Int_32
            log(2, "ptr[13] =", hex(ptr[0x13]))
            assert(ptr[0x13] == 0x57)
            log(2, "ptr[14] =", hex(ptr[0x14]))
            assert(ptr[0x14] == 0x34)
            log(2, "ptr[15] =", hex(ptr[0x15]))
            assert(ptr[0x15] == 0x12)
            log(2, "ptr[16] =", hex(ptr[0x16]))
            assert(ptr[0x16] == 0xf0)

            # Ptr
            log(2, "ptr[17] =", hex(ptr[0x17]))
            assert(ptr[0x17] == 0)
            log(2, "ptr[18] =", hex(ptr[0x18]))
            assert(ptr[0x18] == 0)
            log(2, "ptr[19] =", hex(ptr[0x19]))
            assert(ptr[0x19] == 0)
            log(2, "ptr[1a] =", hex(ptr[0x1a]))
            assert(ptr[0x1a] == 0)
            log(2, "ptr[1b] =", hex(ptr[0x1b]))
            assert(ptr[0x1b] == 0)
            log(2, "ptr[1c] =", hex(ptr[0x1c]))
            assert(ptr[0x1c] == 0)
            log(2, "ptr[1d] =", hex(ptr[0x1d]))
            assert(ptr[0x1d] == 0)
            log(2, "ptr[1e] =", hex(ptr[0x1e]))
            assert(ptr[0x1e] == 0)

            # Bit0-63 = 0xA9 69 69 69 69 6A 96 D3
            log(2, "ptr[1f] =", hex(ptr[0x1f]))
            assert(ptr[0x1f] == 0xd3)
            log(2, "ptr[20] =", hex(ptr[0x20]))
            assert(ptr[0x20] == 0x96)
            log(2, "ptr[21] =", hex(ptr[0x21]))
            assert(ptr[0x21] == 0x6a)
            log(2, "ptr[22] =", hex(ptr[0x22]))
            assert(ptr[0x22] == 0x69)
            log(2, "ptr[23] =", hex(ptr[0x23]))
            assert(ptr[0x23] == 0x69)
            log(2, "ptr[24] =", hex(ptr[0x24]))
            assert(ptr[0x24] == 0x69)
            log(2, "ptr[25] =", hex(ptr[0x25]))
            assert(ptr[0x25] == 0x69)
            log(2, "ptr[26] =", hex(ptr[0x26]))
            assert(ptr[0x26] == 0xa9)

            # Int_n
            log(2, "ptr[27] =", hex(ptr[0x27]))
            assert(ptr[0x27] == 0x10)
            log(2, "ptr[28] =", hex(ptr[0x28]))
            assert(ptr[0x28] == 0x21)
            log(2, "ptr[29] =", hex(ptr[0x29]))
            assert(ptr[0x29] == 0x43)
            log(2, "ptr[2a] =", hex(ptr[0x2a]))
            assert(ptr[0x2a] == 0x65)
            log(2, "ptr[2b] =", hex(ptr[0x2b]))
            assert(ptr[0x2b] == 0x87)
            log(2, "ptr[2c] =", hex(ptr[0x2c]))
            assert(ptr[0x2c] == 0xa9)
            log(2, "ptr[2d] =", hex(ptr[0x2d]))
            assert(ptr[0x2d] == 0xcb)
            log(2, "ptr[2e] =", hex(ptr[0x2e]))
            assert(ptr[0x2e] == 0xed)

            # Update some fields through struct field way and memory way
            log(2, "\n<Field update test>")
            test_data.Int_8 = 31
            log(2, "test_data.Int_8 <=", hex(test_data.Int_8))
            assert(test_data.Int_8 == 31)
            log(2, "ptr[0f] =", hex(ptr[0x0f]))
            assert(ptr[0x0f] == 0xed)
            log(2, "ptr[10] =", hex(ptr[0x10]))
            assert(ptr[0x10] == 31)
            log(2, "ptr[11] =", hex(ptr[0x11]))
            assert(ptr[0x11] == 0xa9)

            test_data.Int_32 = 0x0fedcba9
            log(2, "test_data.Int_32 <=", hex(test_data.Int_32))
            assert(test_data.Int_32 == 0x0fedcba9)

            log(2, "ptr[12] =", hex(ptr[0x12])) # check if it will cross the field border or not
            assert(ptr[0x12] == 0x4f)
            log(2, "ptr[13] =", hex(ptr[0x13]))
            assert(ptr[0x13] == 0xa9)
            log(2, "ptr[14] =", hex(ptr[0x14]))
            assert(ptr[0x14] == 0xcb)
            log(2, "ptr[15] =", hex(ptr[0x15]))
            assert(ptr[0x15] == 0xed)
            log(2, "ptr[16] =", hex(ptr[0x16]))
            assert(ptr[0x16] == 0x0f)
            log(2, "ptr[17] =", hex(ptr[0x17])) # check if it will cross the field border or not
            assert(ptr[0x17] == 0)

            test_data.Bit1_7 = 0x6e
            log(2, "test_data.Bit1_7 <=", hex(test_data.Bit1_7))
            assert(test_data.Bit1_7 == 0x6e)
            log(2, "test_data.Bit0 =", hex(test_data.Bit0))
            assert(test_data.Bit0 == 1)
            log(2, "test_data.Bit8_15 =", hex(test_data.Bit8_15))
            assert(test_data.Bit8_15 == 0x96)
            log(2, "ptr[1f] =", hex(ptr[0x1f]))
            assert(ptr[0x1f] == 0xdd)
            log(2, "ptr[20] =", hex(ptr[0x20]))
            assert(ptr[0x20] == 0x96)

        test_data.FREE()

    def test_null(self):
        log(1, "\r\n[Null pointer]")

        ptr = uefi.mem("P") # no type given, no memory allocation (aka. it's NULL pointer)
        log(2, "?: ptr == null\r")
        assert(ptr == uefi.null)

        log(2, "?: ptr == 0\r")
        assert(ptr == 0)
        assert(ptr.VALUE == 0)

        addr = 0x12345678
        log(2, "<< ptr  = 0x%x\r" % addr)
        ptr.VALUE = addr
        log(2, "?: ptr == 0x%x\r" % addr)
        assert(ptr == addr)
        log(2, "?: ptr != uefi.null\r")
        assert(ptr != uefi.null)
        assert(ptr.VALUE != 0)

        ptr.FREE()

if __name__ == '__main__':
    mytest = MemBasicUnitTest()

