import sys
import uefi
import edk2
from ucollections import OrderedDict
from unittest import *

EFI_GUID = OrderedDict([
    ("Data1", 'L'),
    ("Data2", 'H'),
    ("Data3", 'H'),
    ("Data4", '8B'),
])

"""
struct date
{
   INT64    Year;    // q
   UINT8    Month;   // B
   INT16    Day;     // h
   UINT16   Hour;    // H
   INT32    Minute;  // l
   UINT32   Second;  // L
   UINT64   Nanosecond;  // Q
   INTN	    TimeZone;   // n
 };
 """


date = OrderedDict([
    ("Year",       'q'),
    ("Month",      'B'),
    ("Day",        'h'),
    ("Hour",       'H'),
	("Minute",     'l'),
    ("Second",     'L'),
    ("Nanosecond", 'Q'),
    ("TimeZone",   'n'),
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

        signed_b = mem('b')
        a = mem('b')
        b = mem('b')
        c = mem('b')
        d = mem('b')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt8(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
		


 

		
    def test_B(self):
        log(1, "\n[%s]" % "B - RETURN UINT8")

        signed_b = mem('B')
        a = mem('B')
        b = mem('B')
        c = mem('B')
        d = mem('B')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint8(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
		
		
		
    def test_h(self):
        log(1, "\n[%s]" % "h - RETURN INT16")

        signed_b = mem('h')
        a = mem('h')
        b = mem('h')
        c = mem('h')
        d = mem('h')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt16(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    

    def test_H(self):
        log(1, "\n[%s]" % "H - RETURN UINT16")

        signed_b = mem('H')
        a = mem('H')
        b = mem('H')
        c = mem('H')
        d = mem('H')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint16(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    
    def test_l(self):
        log(1, "\n[%s]" % "l - RETURN INT32")

        signed_b = mem('l')
        a = mem('l')
        b = mem('l')
        c = mem('l')
        d = mem('l')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt32(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
    

	
    def test_L(self):
        log(1, "\n[%s]" % "L - RETURN UINT32")

        signed_b = mem('L')
        a = mem('L')
        b = mem('L')
        c = mem('L')
        d = mem('L')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint32(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	

  
    def test_q(self):
        log(1, "\n[%s]" % "L - RETURN INT64")

        signed_b = mem('q')
        a = mem('q')
        b = mem('q')
        c = mem('q')
        d = mem('q')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt64(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	
	
    def test_Q(self):
        log(1, "\n[%s]" % "L - RETURN UINT64")

        signed_b = mem('Q')
        a = mem('Q')
        b = mem('Q')
        c = mem('Q')
        d = mem('Q')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUint64(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
	
    def test_i(self):
        log(1, "\n[%s]" % "i - RETURN int")

        signed_b = mem('i')
        a = mem('i')
        b = mem('i')
        c = mem('i')
        d = mem('i')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnInt(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

 
    def test_I(self):
        log(1, "\n[%s]" % "I - RETURN unsigned int")

        signed_b = mem('I')
        a = mem('I')
        b = mem('I')
        c = mem('I')
        d = mem('I')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUnsignedInt(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

		
    def test_n(self):
        log(1, "\n[%s]" % "I - RETURN INTN")

        signed_b = mem('n')
        a = mem('n')
        b = mem('n')
        c = mem('n')
        d = mem('n')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnIntn(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)

 
    def test_N(self):
        log(1, "\n[%s]" % "I - RETURN UINTN")

        signed_b = mem('N')
        a = mem('N')
        b = mem('N')
        c = mem('N')
        d = mem('N')
         
        a.VALUE = 3
        b.VALUE = 1
        c.VALUE = 2
        d.VALUE = 4
		
        sum = uefi.ds.ReturnUintnn(a, b, c, d)
        log(2, "sum =", sum)
        assert(sum == 7)
  
    def test_P(self):
        log(1, "\n[%s]" % "O - struct")
        s = mem("100S", uefi.ds.Returnchar8())
        print (s.VALUE)

        s = mem("100U", uefi.ds.Returnchar16())
        print (s.VALUE)

 #   Infc = mem()
 #   date = mem()
 #   uefi.ds.ReturnPointer (gEfiSmbiosProtocolGuid, null, Infc.LEA())
    def test_PP(self):
        today = mem()
        uefi.ds.ReturnPointer(today.LEA())        
        today.CAST("O#date")
        print ("validate_PP")
        print (hex((today.ADDR)))
        log(2, "Year =", today.Year)
        print (today.Year)
        log(2, "Month =", today.Month)
        print (today.Month)
        log(2, "Day =", today.Day)
        print (today.Day)
        log(2, "Hour =", today.Hour)
        print (today.Hour)
        log(2, "Second =", hex(today.Second))
        print (hex(today.Second))
        log(2, "Nanosecond =", hex(today.Nanosecond))
        print (hex(today.Nanosecond))
        log(2, "TimeZone =", today.TimeZone)
      #  print (today.TimeZone)
	
        

  
    def test_ReturnVariousType(self):
        type = mem("b")
        b = mem("b")
        B = mem("B")
        h = mem("h")
        H = mem("H")
        l = mem("l")
        L = mem("L")
        q = mem("q")
        Q = mem("Q")
        i = mem("i")
        I = mem("I")
        n = mem("n")
        N = mem("N")
 	
        
        b.VALUE = 0x80
        B.VALUE = 0x80
        h.VALUE = 0x8000
        H.VALUE = 0x8000
        l.VALUE = 0x80000000
        L.VALUE = 0x80000000
        q.VALUE = 0x1234567887654321
        Q.VALUE = 0xFFFFFFFFFFFFFFFF
        i.VALUE = 0x80000000
        I.VALUE = 0x80000000
        n.VALUE = 0x80000000
        N.VALUE = 0x12345678
        
        type.VALUE = 1
        sum = uefi.ds.ReturnVariousType(type, b, B, h, H, l, L, q, Q, i)
        log(2, "sum.1 =", hex(sum))        
		
        type.VALUE = 2
        sum = uefi.ds.ReturnVariousType(type, N, n, I, q, Q, l, L, b, B)
        log(2, "sum.2 =", hex(sum))		
		
        type.VALUE = 3
        sum = uefi.ds.ReturnVariousType(type, B, H, L, Q, l, n, b, q, i)		
        log(2, "sum.3 =", hex(sum))

        type.VALUE = 4
        sum = uefi.ds.ReturnVariousType(type, l, n, b, q, i,B, H, L, Q)
        log(2, "sum.4 =", hex(sum))  

        type.VALUE = 5
        sum = uefi.ds.ReturnVariousType(type, L, q, Q, i, b, B, h, H, l)
        log(2, "sum.5 =", hex(sum)) 

        type.VALUE = 6
        sum = uefi.ds.ReturnVariousType(type, Q, l, L, b, B, N, n, I, q,)
        log(2, "sum.6 =", hex(sum)) 
		
if __name__ == '__main__':
    mytest = MemBasicUnitTest()

