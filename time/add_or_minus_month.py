import datetime

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)


datetime_object = datetime.datetime.strptime('Jun 1 2018', '%b %d %Y')
for i in range(-15,15):
    target = monthdelta(datetime_object, i)
    _t = '{0}-{1}-{2}'.format(target.year, target.month, target.day)
    print(_t)
