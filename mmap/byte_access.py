import mmap

f = open('Hello.dex', 'rb')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)


magic           = m[0:8]# 8 byte
checksum        = m[8:0xC]# 4 byte
signiture       = m[0xC:0x20]# 20 byte
file_size       = m[0x20:0x24]# 4 byte

print('magic: 0x{0}'.format(magic.hex()))
print('signiture: 0x{0}'.format(signiture.hex()))
print('file_size: 0x{0}'.format(file_size.hex()))# output:0xd8020000, real size = 728 byte = hex(2d8)
