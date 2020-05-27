import zlib



def compress(data):
    compresslevel=9
    cobj = zlib.compressobj( compresslevel,zlib.DEFLATED,-zlib.MAX_WBITS,zlib.DEF_MEM_LEVEL,0 )
    d = cobj.compress(data)
    d += cobj.flush()
    return d

def decompress(data):
    dobj = zlib.decompressobj( -zlib.MAX_WBITS )
    d = dobj.decompress(data)
    d += dobj.flush()
    return d


# data
data = ['abc']*100

# compress
print('original data = {0}'.format(data))
data = '\n'.join(data)
data = bytes(data, encoding = "utf8")    # str to bytes 
content = compress(data)
print('compress data = {0}'.format(content))

# decompress
data = decompress(content)
data = str(data, encoding = "utf8")      # bytes to str  
print('decompress data = {0}'.format(data))
