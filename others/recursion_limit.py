import sys


# get and set system recursion limit.
default_value = sys.getrecursionlimit()

print('default recursion limit value = {0}'.format(default_value))

sys.setrecursionlimit(default_value+10)


after_value = sys.getrecursionlimit()

print('set recursion limit value = {0} after add 10 to default'.format(after_value))

