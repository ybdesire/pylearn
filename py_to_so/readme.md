# 1. convert python code to so file

0. ref: https://blog.csdn.net/ctwy291314/article/details/88849139
1. mytest.py

```python
class mytest:

    def __init__(self):
        print('init')

    def say(self):
        print ('hello')
```

2. setup.py

```python
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize(["mytest.py"]))
```

3. build the class to so file

```
python setup.py build_ext
```

so we can get so file at : `build/lib.linux-x86_64-cpython-37/mytest.cpython-37m-x86_64-linux-gnu.so`



# 2. python call functions from so file

1. `cd build/lib.linux-x86_64-cpython-37/`
2. python code as below

```python
>>> import ctypes
>>> so = ctypes.CDLL('./mytest.cpython-37m-x86_64-linux-gnu.so')
>>> from mytest import mytest
>>> mytest().say()
init
hello
```


