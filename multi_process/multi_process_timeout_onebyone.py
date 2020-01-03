import numpy as np
import time,os
from multiprocessing import Pool

def worker(x):
    num=x[0]+x[1]+x[2]
    pid = os.getpid()
    xtime = np.random.random()*num*5
    print('started. pid = {0}, num={1}, xtime={2}'.format(pid,num,xtime))
    time.sleep(xtime)
    print('ended. pid = {0}, num={1}, xtime={2}'.format(pid,num,xtime))
    return xtime

def main():

    args = [(1,1,1),(1,2,1),(2,1,2),(0,0,1),(1,0,1),(2,2,2),(6,6,6)]
    for arg in args:
        pool = Pool(1)
        pool_result = pool.map_async(worker, [arg])

        # wait 8s for every worker to finish
        pool_result.wait(timeout=8)

        # once the timeout has finished we can try to get the results
        if pool_result.ready():
            print(pool_result.get(timeout=1))
            print('ended successful for arg={0}'.format(arg))
        else:
            print('ended timeout for arg={0}'.format(arg))
    

if __name__ == "__main__":
    main()
