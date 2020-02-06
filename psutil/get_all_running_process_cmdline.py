import psutil
#Iterate over the all the running process
proc = None
for proc in psutil.process_iter():
    try:
        print(proc.cmdline(), proc.pid, proc.ppid())
    except Exception as e:
        print(e)
