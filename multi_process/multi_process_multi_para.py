import multiprocessing

def worker(l1,l2):
    """thread worker function"""
    print( 'Worker: {0}, {1}'.format(l1,l2) )
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=([1+i,2+i,3+i],[4+i,5+i]))
        p.start()
