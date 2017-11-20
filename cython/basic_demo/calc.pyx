# environment: linx

from libc.stdint cimport float

cimport cython

def fun(r):
    cdef float x
    cdef float y

    x = 3.1415926*r*r
    y = 2*3.14*r
    return x-y
