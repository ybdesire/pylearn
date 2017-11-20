# environment: linx
import time

import pyximport
pyximport.install(
    reload_support=True)
import calc

start_time = time.time()
for i in range(10000000):
    calc.fun(i)
print('costed {} seconds'.format(time.time() - start_time))
