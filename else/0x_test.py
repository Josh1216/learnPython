testNum = 0x10345678

righter = (testNum>>16)
lefter = testNum & 0xFFFF
print(righter)
print(lefter)

pluser = (righter<<16) + lefter
print(hex(pluser))