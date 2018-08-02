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

		
    def test_return(self):
	    log(1, "\n[%s]" % " b - RETURN INT8")
      
		
    def test_b(self):
        log(1, "\n[%s]" % "b - RETURN INT8")

        signed_b = uefi.mem('b')
        a = uefi.mem('b')
        b = uefi.mem('b')
        c = uefi.mem('b')
        d = uefi.mem('b')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt8(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
		


 

		
    def test_B(self):
        log(1, "\n[%s]" % "B - RETURN UINT8")

        signed_b = uefi.mem('B')
        a = uefi.mem('B')
        b = uefi.mem('B')
        c = uefi.mem('B')
        d = uefi.mem('B')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint8(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
		
		
		
    def test_h(self):
        log(1, "\n[%s]" % "h - RETURN INT16")

        signed_b = uefi.mem('h')
        a = uefi.mem('h')
        b = uefi.mem('h')
        c = uefi.mem('h')
        d = uefi.mem('h')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt16(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    

    def test_H(self):
        log(1, "\n[%s]" % "H - RETURN UINT16")

        signed_b = uefi.mem('H')
        a = uefi.mem('H')
        b = uefi.mem('H')
        c = uefi.mem('H')
        d = uefi.mem('H')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint16(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    
    def test_l(self):
        log(1, "\n[%s]" % "l - RETURN INT32")

        signed_b = uefi.mem('l')
        a = uefi.mem('l')
        b = uefi.mem('l')
        c = uefi.mem('l')
        d = uefi.mem('l')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt32(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    

	
    def test_L(self):
        log(1, "\n[%s]" % "L - RETURN UINT32")

        signed_b = uefi.mem('L')
        a = uefi.mem('L')
        b = uefi.mem('L')
        c = uefi.mem('L')
        d = uefi.mem('L')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint32(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	

  
    def test_q(self):
        log(1, "\n[%s]" % "L - RETURN INT64")

        signed_b = uefi.mem('q')
        a = uefi.mem('q')
        b = uefi.mem('q')
        c = uefi.mem('q')
        d = uefi.mem('q')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt64(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	
	
    def test_Q(self):
        log(1, "\n[%s]" % "L - RETURN UINT64")

        signed_b = uefi.mem('Q')
        a = uefi.mem('Q')
        b = uefi.mem('Q')
        c = uefi.mem('Q')
        d = uefi.mem('Q')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint64(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	
    def test_i(self):
        log(1, "\n[%s]" % "i - RETURN int")

        signed_b = uefi.mem('i')
        a = uefi.mem('i')
        b = uefi.mem('i')
        c = uefi.mem('i')
        d = uefi.mem('i')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

 
    def test_I(self):
        log(1, "\n[%s]" % "I - RETURN unsigned int")

        signed_b = uefi.mem('I')
        a = uefi.mem('I')
        b = uefi.mem('I')
        c = uefi.mem('I')
        d = uefi.mem('I')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUnsignedInt(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

		
    def test_n(self):
        log(1, "\n[%s]" % "I - RETURN INTN")

        signed_b = uefi.mem('n')
        a = uefi.mem('n')
        b = uefi.mem('n')
        c = uefi.mem('n')
        d = uefi.mem('n')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnIntn(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

 
    def test_N(self):
        log(1, "\n[%s]" % "I - RETURN UINTN")

        signed_b = uefi.mem('N')
        a = uefi.mem('N')
        b = uefi.mem('N')
        c = uefi.mem('N')
        d = uefi.mem('N')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUintnn(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
  
    def test_P(self):
        log(1, "\n[%s]" % "O - struct")
        s = uefi.mem("100S", uefi.ds.Returnchar8())
        print (s.VALUE)

        s = uefi.mem("100U", uefi.ds.Returnchar16())
        print (s.VALUE)


     
    


if __name__ == '__main__':
    mytest = MemBasicUnitTest()

