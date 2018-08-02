import sys
import uefi
from ucollections import OrderedDict
from unittest import *

class RuntimeServiceUnitTest(TestCase):
    def setUp(self):
        log(0, "[EFI_RUNTIME_SERVICES: BEGIN]")

    def tearDown(self):
        log(0, "\n[EFI_RUNTIME_SERVICES: PASS]")

    def test_Hdr(self):
        log(1, "Hdr.Signature  =", hex(uefi.rt.Hdr.Signature))
        assert(uefi.rt.Hdr.Signature == 0x56524553544e5552)
        log(1, "Hdr.Revision   =", hex(uefi.rt.Hdr.Revision))
        assert(uefi.rt.Hdr.Revision == 0x20046)
        log(1, "Hdr.HeaderSize =", hex(uefi.rt.Hdr.HeaderSize))
        assert(uefi.rt.Hdr.HeaderSize == 0x88)
        log(1, "Hdr.CRC32      =", hex(uefi.rt.Hdr.CRC32))

    # GetTime
    def test_GetTime(self):
        log(1, "\r\n[GetTime]")
        time = uefi.mem("O#uefi.EFI_TIME")
        uefi.rt.GetTime(time, uefi.null)
        log(2, "Year       =", time.Year)
        log(2, "Month      =", time.Month)
        log(2, "Day        =", time.Day)
        log(2, "Hour       =", time.Hour)
        log(2, "Minute     =", time.Minute)
        log(2, "Second     =", time.Second)
        log(2, "Nanosecond =", time.Nanosecond)
        log(2, "TimeZone   =", time.TimeZone)
        log(2, "Daylight   =", time.Daylight)
        time.FREE()

    # GetVariable
    def test_GetVariable(self):
        log(1, "\r\n[GetVariable]")

        varguid = uefi.guid("8be4df61-93ca-11d2-aa0d-00e098032b8c")
        size = uefi.mem('N')
        size.VALUE = 0
        try:
            #                   T     i     m     e     o     u     t
            uefi.rt.GetVariable("\u0054\u0069\u006d\u0065\u006f\u0075\u0074", varguid.REF(), uefi.null, size.REF(), uefi.null)
        except uefi.efistatus as Excpt:
            if "BUFFER_TOO_SMALL" not in Excpt.args[0]:
                assert(False)
            assert(size.VALUE > 0)

        data = uefi.mem('%dB' % size.VALUE)
        uefi.rt.GetVariable("Timeout", varguid, uefi.null, size, data)
        print('    Timeout = ', end='')
        for v in data:
            print(v, end=' ')
        print('\r\n')

        data.FREE()
        size.FREE()

    # GetNextVariableName
    def test_GetNextVariableName(self):
        log(1, "\r\n[GetNextVariableName]")

        size = uefi.mem('N')
        name = uefi.mem('128H')
        log(2, "len(name) =", len(name))
        name.CAST('U')  # Convert to unicode string for print purpose
        name.VALUE = ""     # For the first time calling of GetNextVariableName, an empty string must be given.
        varguid = uefi.guid("00000000-0000-0000-0000-000000000000")
        log(2, "len(name) =", len(name))
        log(2, "len(guid) =", len(varguid), varguid.VALUE)

        while True:
            try:
                size.VALUE = len(name)
                uefi.rt.GetNextVariableName(size, name, varguid)
                log(2, "Found variable:", varguid, name.VALUE)
            except uefi.efistatus as Excpt:
                log (2, str(Excpt))
                break

        varname = bytearray(name)
        size.FREE()
        name.FREE()
        varguid.FREE()

        print(varname, len(varname))

    def test_VariableStorage(self):
        log(1, "\r\n[VariableStorage class]")
        vs = uefi.VariableStorage()
        for name,guid in vs:
            log(2, "Found variable:", guid, name)
            
        log(1, "Variables of vendor=8BE4DF61-93CA-11D2-AA0D-00E098032B8C")
        vendor_vs = uefi.VariableStorage("8BE4DF61-93CA-11D2-AA0D-00E098032B8C")
        for name in vendor_vs:
            log(2, "Found variable:", name, "size =", len(vendor_vs[name]))

        myvar = ("MyTest", "8955FE9B-FD9A-4B79-999A-2F169AC22FA9")
        value = vs[myvar]
        log(2, "MyTest =", value)
        log(2, "MyTest in VariableStorage is", myvar in vs)

        value = [1, 2, 3, 4, 5, 6, 7]
        log(2, "Create MyTest =", value)
        vs[myvar] = value
        log(2, "MyTest =", list(vs[myvar]))
        log(2, "MyTest in VariableStorage is", myvar in vs)

        value[0] = 7
        value[1] = 6
        value[2] = 5
        value[3] = 4
        value[4] = 3
        value[5] = 2
        value[6] = 1
        log(2, "Change to [7, 6, 5, 4, 3, 2, 1]")
        vs[myvar] = value
        log(2, "MyTest =", list(vs[myvar]))

        del vs[myvar]
        log(2, "Delete MyTest")
        log(2, "MyTest =", vs[myvar])
        log(2, "MyTest in VariableStorage is", myvar in vs)

if __name__ == '__main__':
    mytest = RuntimeServiceUnitTest()

