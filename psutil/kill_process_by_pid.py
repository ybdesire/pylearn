import psutil
pid = 666688886666
p = psutil.Process(pid)
p.terminate()  #or p.kill()
