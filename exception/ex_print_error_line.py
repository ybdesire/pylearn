import sys


try:
    x = 1+1
    y = x/0
    z = 2+2

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))