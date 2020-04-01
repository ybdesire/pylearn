import hashlib

s = 'hello'

sha1 = hashlib.sha1(str(s).encode('utf-8')).hexdigest()
print(sha1)
#'aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d'
sha256 = hashlib.sha256(str(s).encode('utf-8')).hexdigest()
print(sha256)
#'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'

