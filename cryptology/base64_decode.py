import base64
# python3

x = b'cG9zc2libHkgYmFzZTY0IGVuY29kZWQgc3RyaW5n'
y = base64.b64decode(x)
print('base64 decode: ')
print(y)
# b'possibly base64 encoded string'