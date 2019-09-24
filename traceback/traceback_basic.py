import traceback

print('before traceback')
try:
    1/0
except Exception as e:
    print(e)

print()
# get more detail exception
print('after traceback')
try:
    1/0
except Exception as e:
    traceback.print_exc()


