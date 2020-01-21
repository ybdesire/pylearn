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

    pool = Pool(3)# max 3 processes
    args = [(1,1,1),(1,2,1),(2,1,2),(0,0,1),(1,0,1),(2,2,2),(6,6,6)]
    pool_result = pool.map_async(worker, args)

    # wait 8s for every worker to finish
    pool_result.wait(timeout=8)# 8s for 3 processes

    # once the timeout has finished we can try to get the results
    if pool_result.ready():
        print(pool_result.get(timeout=1))
    print('ended main')
    

if __name__ == "__main__":
    main()
