import pendulum


now_in_china = pendulum.now('Asia/Chongqing')
print(now_in_china)


dt_toronto = pendulum.datetime(2012, 1, 1, tz='America/Toronto')
print(dt_toronto)



