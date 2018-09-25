import datetime

n1 = datetime.datetime.now()

j=0
for i in range(1000000):
    j+=1

n2 = datetime.datetime.now()


n = n2-n1
seconds = n.total_seconds()


print(seconds)