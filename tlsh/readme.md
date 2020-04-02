1. what it is ?

https://github.com/trendmicro/tlsh


2. how to buid it ?

* linux install cmake
* clone tlsh code

```
git clone git://github.com/trendmicro/tlsh.git
cd tlsh
git checkout master
```

* make and install python interface

```
$./make.sh
$ cd py_ext/
$ python ./setup.py build
$ python ./setup.py install

```


3. code by python

```python
import tlsh
data = 'asd0000000000000000000000000fsd0fasdfa8f9asdfa8d897987a89df9878*&&(^&fsadvasdv'
result = tlsh.hash(data)
print(result)

#'63A002E650455445D22E4350404D3B42FE46398550F2954684C1B410895DEE8F8D0A55'
```