import os
import psutil
process = psutil.Process(os.getpid())
print(process.memory_info().rss)
# https://stackoverflow.com/questions/938733/total-memory-used-by-python-process