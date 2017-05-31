def memory_usage_psutil():
    # return the memory usage in MB
    import psutil,os
    process = psutil.Process(os.getpid())
    mem = process.memory_info()[0] / float(2 ** 20)
    return mem

x = [0]*100000000
print( 'The memory usage by this process is {0}MB'.format(memory_usage_psutil()) )