import threading

# global var
count = 0
lock = threading.Lock()

# Define a function for the thread
def print_time(threadName):
    global count
    
    c=0
    with lock:
        while(c<100):
            c+=1
            count+=1
            print("{0}: set count to {1}".format( threadName, count) )

# Create and run threads as follows
try:
    threading.Thread( target=print_time, args=("Thread-1", ) ).start()
    threading.Thread( target=print_time, args=("Thread-2", ) ).start()
    threading.Thread( target=print_time, args=("Thread-3", ) ).start()
except Exception as e:
    print("Error: unable to start thread")

