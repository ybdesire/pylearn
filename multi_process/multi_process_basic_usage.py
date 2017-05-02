import multiprocessing

def worker():
    """worker function"""
    print('Worker')
    return

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        p.start()
