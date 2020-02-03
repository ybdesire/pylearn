import psutil
#Iterate over the all the running process
for proc in psutil.process_iter():
    try:
        print(proc.name().lower())
    except Exception as e:
        print(e)