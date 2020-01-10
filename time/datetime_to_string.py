import datetime

date_time = datetime.datetime.now()
print(date_time)
d1 = date_time.strftime("%m/%d/%Y")
print(d1)
d2 = date_time.strftime("%H:%M:%S")
print(d2)
d3 = date_time.strftime("%m/%d/%Y%H:%M:%S")
print(d3)

'''
2020-01-10 02:51:37.810641
01/10/2020
02:51:37
01/10/202002:51:37
'''