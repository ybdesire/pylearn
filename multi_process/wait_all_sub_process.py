from multiprocessing import Pool

def worker(num):
    print("worker working ", num)

if __name__=='__main__':
    p = Pool()
    for i in range(5):
        p.apply_async(worker, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
