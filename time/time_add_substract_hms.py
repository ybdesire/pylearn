import datetime

now = datetime.datetime.now()

tm1 = now + datetime.timedelta(hours=8)
tm2 = now + datetime.timedelta(minutes=8)
tm3 = now + datetime.timedelta(seconds=8)
tm4 = now + datetime.timedelta(hours=8,minutes=8,seconds=8)

print(tm1)
print(tm2)
print(tm3)
print(tm4)


'''
2018-08-25 16:04:17.469511
2018-08-25 08:12:17.469511
2018-08-25 08:04:25.469511
2018-08-25 16:12:25.469511
'''

