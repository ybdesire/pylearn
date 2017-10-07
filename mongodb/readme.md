# mongo db basic


## windows client

* MongoChef


## pymongo

Eaxmple document schema

```
{
    'sha1': '001',
    'time': '2014-12-08T04:02:32.329Z',
    'content': 'abc bcd'
}

{
    'sha1': '002',
    'time': '2015-12-08T04:02:32.329Z',
    'content': 'bax abc ccd'
}

{
    'sha1': '003',
    'time': '2016-12-08T04:02:32.329Z',
    'content': 'axabcdgsdf'
}

```

Below code all based on this schema.


## basic

* [insert_one](insert_one.py)
* [remove](remove.py)
* [update](https://stackoverflow.com/questions/13710770/how-to-update-values-using-pymongo)
* [find_one](find_one.py)
* [find_all](find_all.py)


## useful

* [find by time period](find_by_time_period.py)


## fuzzy maching by re

```
import re
rexExp = re.compile('.*' + 'abc' + '.*', re.IGNORECASE)  # 匹配除换行符 \n 之外的任何单字符, 0次或多次
res = db.find({'content':rexExp })  
for rs in res:  
    print(rs)
```





