import time
import timeout_decorator

@timeout_decorator.timeout(3)
def mytest():
    print("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{} seconds have passed".format(i))

if __name__ == '__main__':
    try:
        mytest()
    except timeout_decorator.timeout_decorator.TimeoutError as e:
        print('timeout exception')
