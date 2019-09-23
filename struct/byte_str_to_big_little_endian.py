import struct

x = b'\x78\x56\x34\x12'


# L: unsigned long, 4 byte
# >: big-endian
# <: little-endian
x_big_endian = struct.unpack('>L', x) 
x_little_endian = struct.unpack('<L', x) 

print(x_big_endian)# treated as 0x78563412
print(x_little_endian)# treated as 0x12345678

'''
(2018915346,)
(305419896,)
'''