import multiprocessing

def worker(num):
    """thread worker function"""
    print( 'Worker: {0}'.format(num) )
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        p.start()
