import uefi

count = uefi.mem("I")
uefi.rt.GetNextHighMonotonicCount(count.REF())
print(count.VALUE)
count.FREE()
