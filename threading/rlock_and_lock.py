import threading

# change from RLock to Lock, get deadlock
lock = threading.RLock()

def f():
  with lock:
    g()
    h()

def g():
  with lock:
    h()
    do_something1()

def h():
  with lock:
    do_something2()

def do_something1():
    print('do_something1')

def do_something2():
    print('do_something2')

# Create and run threads as follows
try:
    threading.Thread( target=f ).start()
    threading.Thread( target=f ).start()
    threading.Thread( target=f ).start()
except Exception as e:
    print("Error: unable to start thread")

