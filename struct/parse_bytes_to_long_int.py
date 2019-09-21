import struct

data = b'\x00\x01\x00\x02'

# parse 4 byte as little endian as long/int
value_long = struct.unpack('<L', data)[0]#4byte, hex(02000100) = dec(33554688)
value_int = struct.unpack('<I', data)[0]#4byte

print('parsed as long: {0}'.format(value_long))
print('parsed as int: {0}'.format(value_int))

'''
parsed as long: 33554688
parsed as int: 33554688
'''
