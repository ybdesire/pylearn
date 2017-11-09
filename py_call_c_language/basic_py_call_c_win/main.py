from ctypes import *
import os
libtest = cdll.LoadLibrary('libtest.dll')
print(libtest.multiply(2, 2))
