import traceback

def fun2():
    1/0

def fun():
    fun2()

# get more detail exception
print('after traceback')
try:
    fun()
except Exception as e:
    msg = traceback.format_exc()
    print(msg)
