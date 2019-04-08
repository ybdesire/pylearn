import base64
# python3

x = b'possibly base64 encoded string'
y = base64.b64encode(x)
print('base64 encoding: ')
print(y)
# b'cG9zc2libHkgYmFzZTY0IGVuY29kZWQgc3RyaW5n'