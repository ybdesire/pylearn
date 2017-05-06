import multiprocessing
import time, os



def worker():
    name = multiprocessing.current_process().name
    pid = os.getpid()
    print('Starting process: {0},{1}'.format(name, pid))
    time.sleep(2)
    print('Exiting process: {0},{1}'.format(name, pid))



def my_service():
    name = multiprocessing.current_process().name
    pid = os.getpid()
    print('Starting process: {0},{1}'.format(name, pid))
    time.sleep(3)
    print('Exiting process: {0},{1}'.format(name, pid))



if __name__ == '__main__':
    service = multiprocessing.Process(name='my_service', target=my_service)
    worker_1 = multiprocessing.Process(name='worker 1', target=worker)
    worker_2 = multiprocessing.Process(target=worker) # use default name

    worker_1.start()
    worker_2.start()
    service.start()

'''
Starting process: worker 1,30724
Starting process: Process-3,33964
Starting process: my_service,17744
Exiting process: worker 1,30724
Exiting process: Process-3,33964
Exiting process: my_service,17744
'''