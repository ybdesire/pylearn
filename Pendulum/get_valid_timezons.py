import pendulum


# get valid timezon
# https://pendulum.eustace.io/blog/pendulum-1-3-0-is-out.html
print(pendulum.timezones)


# find China
for t in pendulum.timezones:
    if('Chongqing' in t):
        print(t)