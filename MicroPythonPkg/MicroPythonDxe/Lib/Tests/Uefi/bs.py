import sys
import uefi
from ucollections import OrderedDict
from unittest import *

TEST_PROTOCOL1 = OrderedDict(
  (
    ("Signature", "Q"),
    ("Revision", "I"),
  )
)
TEST_PROTOCOL2 = OrderedDict(
  (
    ("Signature", "Q"),
    ("Revision", "I"),
    ("Data", "I"),
  )
)

class BootServiceUnitTest(TestCase):
    def setUp(self):
        log(0, "[UEFI_BOOT_SERVICES: BEGIN]")

    def tearDown(self):
        log(0, "\n[UEFI_BOOT_SERVICES: PASS]")

    def test_GetNextMonotonicCount(self):
        log(1, "\r\n[gBS->GetNextMonotonicCount()]")

        # use explicit way
        count1 = uefi.mem()
        uefi.bs.AllocatePool(uefi.EfiBootServicesData, 8, count1.REF().REF())
        uefi.bs.GetNextMonotonicCount(count1)

        count1.CAST("8B")
        log(2, "count1[] =", hex(count1[0]), hex(count1[1]), hex(count1[2]), hex(count1[3]), hex(count1[4]), hex(count1[5]), hex(count1[6]), hex(count1[7]))

        count1.CAST("Q")
        log(2, "count1 =", hex(count1.VALUE))

        # use implicit way
        count2 = uefi.mem('Q')  # This will allocate memmory with gBS->AllocatePool()
        uefi.bs.GetNextMonotonicCount(count2.REF())
        log(2, "count2 =", hex(count2.VALUE))
        assert(count2.VALUE == (count1.VALUE + 1))

        count1.FREE()
        count2.FREE()

    def test_ProtocolBasic(self):
        log(1, "\r\n[Protocol Basic Test: Check SimpleFileSystemProtocol]")

        gEfiSimpleFileSystemProtocolGuid = uefi.guid("964E5B22-6459-11D2-8E39-00A0C969723B")
        gEfiFileSystemVolumeLabelInfoIdGuid = uefi.guid("DB47D7D3-FE81-11D3-9A35-0090273FC14D")

        HandleCount = uefi.mem("N")
        HandleBuffer = uefi.mem()
        SimpleFsProtocol = uefi.mem()
        Root = uefi.mem()
        Label = uefi.mem("32u")
        LabelLength = uefi.mem("N")
        LabelLength.VALUE = Label.SIZE

        uefi.bs.LocateHandleBuffer(uefi.ByProtocol, gEfiSimpleFileSystemProtocolGuid, 0, HandleCount, HandleBuffer.REF().REF())
        HandleBuffer.CAST("%dPT" % HandleCount.VALUE)
        log(2, "    Handle count:", HandleCount.VALUE)

        for i in range(HandleCount.VALUE):
            log(2, "    Handle", i, "=", hex(HandleBuffer[i].VALUE), HandleBuffer[i].TYPE)
            uefi.bs.HandleProtocol(HandleBuffer[i].REF(), gEfiSimpleFileSystemProtocolGuid, SimpleFsProtocol.REF().REF())

            SimpleFsProtocol.CAST("O#uefi.EFI_SIMPLE_FILE_SYSTEM_PROTOCOL")
            SimpleFsProtocol.OpenVolume(SimpleFsProtocol, Root.REF().REF())

            Root.CAST("O#uefi.EFI_FILE_PROTOCOL")
            Root.GetInfo(Root, gEfiFileSystemVolumeLabelInfoIdGuid, LabelLength, Label)
            log(3, "    Simple file system", i, "label:", Label.VALUE)

        HandleBuffer.FREE()
        gEfiSimpleFileSystemProtocolGuid.FREE()
        gEfiFileSystemVolumeLabelInfoIdGuid.FREE()
        HandleCount.FREE()
        Label.FREE()
        LabelLength.FREE()

    def test_InstallMultipleProtocolInterfaces(self):
        log(1, "\r\n[Protocol Advanced Test: InstallMultipleProtocolInterfaces]")

        tp1 = uefi.mem("O#TEST_PROTOCOL1")
        tp2 = uefi.mem("O#TEST_PROTOCOL2")

        tp1.Signature = 0x3154534554 #TEST1
        tp1.Revision = 1

        tp2.Signature = 0x3254534554 #TEST2
        tp2.Revision = 2
        tp2.Data = 0x12345678

        tp1guid = uefi.guid("BF334812-8990-4296-A2EF-C45B4E6D1A90")
        tp2guid = uefi.guid("50142D13-8302-4C29-B12C-267A860B301D")
        status = uefi.bs.InstallMultipleProtocolInterfaces(
                    uefi.gThis.REF(),
                    tp1guid,
                    tp1,
                    tp2guid,
                    tp2,
                    uefi.mem("P") #uefi.null
                    )
        #assert(status == 0)
        log(2, "Installed protocol 1: GUID=%s" % str(tp1guid))
        log(2, "                      Signature=%x" % tp1.Signature)
        log(2, "                      Revision=%x" % tp1.Revision)
        log(2, "Installed protocol 2: GUID=%s" % str(tp2guid))
        log(2, "                      Signature=%x" % tp2.Signature)
        log(2, "                      Revision=%x" % tp2.Revision)
        log(2, "                      Data=%x" % tp2.Data)

        tp1ptr = uefi.mem("PO#TEST_PROTOCOL1")
        status = uefi.bs.LocateProtocol(tp1guid, uefi.null, tp1ptr.REF())
        log(2, "Locate protocol: %s" % str(tp1guid))
        #assert(status == 0)
        tp1_loc = tp1ptr.DREF()
        log(2, "                 Signature=%x" % tp1.Signature)
        assert (tp1_loc.Signature == 0x3154534554)
        log(2, "                 Revision=%x" % tp1.Revision)
        assert (tp1_loc.Revision == 1)

        tp2ptr = uefi.mem("PO#TEST_PROTOCOL2")
        status = uefi.bs.LocateProtocol(tp2guid, uefi.null, tp2ptr.REF())
        log(2, "Locate protocol: %s" % str(tp2guid))
        #assert(status == 0)
        tp2_loc = tp2ptr.DREF()
        log(2, "                 Signature=%x" % tp2.Signature)
        assert (tp2_loc.Signature == 0x3254534554)
        log(2, "                 Revision=%x" % tp2.Revision)
        assert (tp2_loc.Revision == 2)
        log(2, "                 Data=%x" % tp2.Data)
        assert (tp2_loc.Data == 0x12345678)

        uefi.bs.UninstallMultipleProtocolInterfaces(uefi.gThis, tp1guid, tp1_loc, tp2guid, tp2_loc, uefi.null)
        tp1.FREE()
        tp2.FREE()
        tp1guid.FREE()
        tp2guid.FREE()
        tp1ptr.FREE()
        tp2ptr.FREE()

    def test_Constants(self):
        log(1, "\r\n[Enumeration constants]")

        assert(uefi.AllHandles == 0)
        log(2, "AllHandles == %d" % uefi.AllHandles)

        assert(uefi.ByRegisterNotify == 1)
        log(2, "ByRegisterNotify == %d" % uefi.ByRegisterNotify)

        assert(uefi.ByProtocol == 2)
        log(2, "ByProtocol == %d" % uefi.ByProtocol)

        assert(uefi.AllocateAnyPages == 0)
        log(2, "AllocateAnyPages == %d" % uefi.AllocateAnyPages)

        assert(uefi.AllocateMaxAddress == 1)
        log(2, "AllocateMaxAddress == %d" % uefi.AllocateMaxAddress)

        assert(uefi.AllocateAddress == 2)
        log(2, "AllocateAddress == %d" % uefi.AllocateAddress)

        assert(uefi.TimerCancel == 0)
        log(2, "TimerCancel == %d" % uefi.TimerCancel)

        assert(uefi.TimerPeriodic == 1)
        log(2, "TimerPeriodic == %d" % uefi.TimerPeriodic)

        assert(uefi.TimerRelative == 2)
        log(2, "TimerRelative == %d" % uefi.TimerRelative)

        assert(uefi.EFI_NATIVE_INTERFACE == 0)
        log(2, "EFI_NATIVE_INTERFACE == %d" % uefi.EFI_NATIVE_INTERFACE)

        assert(uefi.EfiReservedMemoryType == 0)
        log(2, "EfiReservedMemoryType == %d" % uefi.EfiReservedMemoryType)

        assert(uefi.EfiLoaderCode == 1)
        log(2, "EfiLoaderCode == %d" % uefi.EfiLoaderCode)

        assert(uefi.EfiLoaderData == 2)
        log(2, "EfiLoaderData == %d" % uefi.EfiLoaderData)

        assert(uefi.EfiBootServicesCode == 3)
        log(2, "EfiBootServicesCode == %d" % uefi.EfiBootServicesCode)

        assert(uefi.EfiBootServicesData == 4)
        log(2, "EfiBootServicesData == %d" % uefi.EfiBootServicesData)

        assert(uefi.EfiRuntimeServicesCode == 5)
        log(2, "EfiRuntimeServicesCode == %d" % uefi.EfiRuntimeServicesCode)

        assert(uefi.EfiRuntimeServicesData == 6)
        log(2, "EfiRuntimeServicesData == %d" % uefi.EfiRuntimeServicesData)

        assert(uefi.EfiConventionalMemory == 7)
        log(2, "EfiConventionalMemory == %d" % uefi.EfiConventionalMemory)

        assert(uefi.EfiUnusableMemory == 8)
        log(2, "EfiUnusableMemory == %d" % uefi.EfiUnusableMemory)

        assert(uefi.EfiACPIReclaimMemory == 9)
        log(2, "EfiACPIReclaimMemory == %d" % uefi.EfiACPIReclaimMemory)

        assert(uefi.EfiACPIMemoryNVS == 10)
        log(2, "EfiACPIMemoryNVS == %d" % uefi.EfiACPIMemoryNVS)

        assert(uefi.EfiMemoryMappedIO == 11)
        log(2, "EfiMemoryMappedIO == %d" % uefi.EfiMemoryMappedIO)

        assert(uefi.EfiMemoryMappedIOPortSpace == 12)
        log(2, "EfiMemoryMappedIOPortSpace == %d" % uefi.EfiMemoryMappedIOPortSpace)

        assert(uefi.EfiPalCode == 13)
        log(2, "EfiPalCode == %d" % uefi.EfiPalCode)

        assert(uefi.EfiPersistentMemory == 14)
        log(2, "EfiPersistentMemory == %d" % uefi.EfiPersistentMemory)

        assert(uefi.EfiResetCold == 0)
        log(2, "EfiResetCold == %d" % uefi.EfiResetCold)

        assert(uefi.EfiResetWarm == 1)
        log(2, "EfiResetWarm == %d" % uefi.EfiResetWarm)

        assert(uefi.EfiResetShutdown == 2)
        log(2, "EfiResetShutdown == %d" % uefi.EfiResetShutdown)

        assert(uefi.EfiResetPlatformSpecific == 3)
        log(2, "EfiResetPlatformSpecific == %d" % uefi.EfiResetPlatformSpecific)

        assert(uefi.EfiGcdMemoryTypeNonExistent == 0)
        log(2, "EfiGcdMemoryTypeNonExistent == %d" % uefi.EfiGcdMemoryTypeNonExistent)

        assert(uefi.EfiGcdMemoryTypeReserved == 1)
        log(2, "EfiGcdMemoryTypeReserved == %d" % uefi.EfiGcdMemoryTypeReserved)

        assert(uefi.EfiGcdMemoryTypeSystemMemory == 2)
        log(2, "EfiGcdMemoryTypeSystemMemory == %d" % uefi.EfiGcdMemoryTypeSystemMemory)

        assert(uefi.EfiGcdMemoryTypeMemoryMappedIo == 3)
        log(2, "EfiGcdMemoryTypeMemoryMappedIo == %d" % uefi.EfiGcdMemoryTypeMemoryMappedIo)

        assert(uefi.EfiGcdMemoryTypePersistentMemory == 4)
        log(2, "EfiGcdMemoryTypePersistentMemory == %d" % uefi.EfiGcdMemoryTypePersistentMemory)

        assert(uefi.EfiGcdMemoryTypeMoreReliable == 5)
        log(2, "EfiGcdMemoryTypeMoreReliable == %d" % uefi.EfiGcdMemoryTypeMoreReliable)

        assert(uefi.EfiGcdMemoryTypeMaximum == 6)
        log(2, "EfiGcdMemoryTypeMaximum == %d" % uefi.EfiGcdMemoryTypeMaximum)

        assert(uefi.EfiGcdIoTypeNonExistent == 0)
        log(2, "EfiGcdIoTypeNonExistent == %d" % uefi.EfiGcdIoTypeNonExistent)

        assert(uefi.EfiGcdIoTypeReserved == 1)
        log(2, "EfiGcdIoTypeReserved == %d" % uefi.EfiGcdIoTypeReserved)

        assert(uefi.EfiGcdIoTypeIo == 2)
        log(2, "EfiGcdIoTypeIo == %d" % uefi.EfiGcdIoTypeIo)

        assert(uefi.EfiGcdIoTypeMaximum == 3)
        log(2, "EfiGcdIoTypeMaximum == %d" % uefi.EfiGcdIoTypeMaximum)

        assert(uefi.EfiGcdAllocateAnySearchBottomUp == 0)
        log(2, "EfiGcdAllocateAnySearchBottomUp == %d" % uefi.EfiGcdAllocateAnySearchBottomUp)

        assert(uefi.EfiGcdAllocateMaxAddressSearchBottomUp == 1)
        log(2, "EfiGcdAllocateMaxAddressSearchBottomUp == %d" % uefi.EfiGcdAllocateMaxAddressSearchBottomUp)

        assert(uefi.EfiGcdAllocateAddress == 2)
        log(2, "EfiGcdAllocateAddress == %d" % uefi.EfiGcdAllocateAddress)

        assert(uefi.EfiGcdAllocateAnySearchTopDown == 3)
        log(2, "EfiGcdAllocateAnySearchTopDown == %d" % uefi.EfiGcdAllocateAnySearchTopDown)

        assert(uefi.EfiGcdAllocateMaxAddressSearchTopDown == 4)
        log(2, "EfiGcdAllocateMaxAddressSearchTopDown == %d" % uefi.EfiGcdAllocateMaxAddressSearchTopDown)

        assert(uefi.EfiGcdMaxAllocateType == 5)
        log(2, "EfiGcdMaxAllocateType == %d" % uefi.EfiGcdMaxAllocateType)

    def test_TPL(self):
        log(1, "\r\n[TPL Test]")

        log(2, "Raise TPL to 10")
        oldtpl = uefi.bs.RaiseTPL(10)
        log(2, "Old TPL =", oldtpl)
        newtpl = uefi.bs.RaiseTPL(15)
        log(2, "New TPL =", newtpl)
        assert (newtpl == 10)
        uefi.bs.RestoreTPL(oldtpl)

if __name__ == '__main__':
    mytest = BootServiceUnitTest()

