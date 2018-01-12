import time

def main():
    x=0
    for i in range(30000000):
        x+=1

if __name__=='__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print('time cost : {0}s'.format(end_time - start_time))
    #time cost : 1.9801132678985596s