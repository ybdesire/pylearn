import pymongo
import re

host="10.11.0.1:27017"
dbname="my_db"
collname="my_collection"
username="my_username"
passwd="my_password"

try:

    client = pymongo.MongoClient(host)
    client.the_database.authenticate(username, passwd, source=dbname)

    db = client[dbname]
    collection = db[collname]

    rexExp = re.compile('.*' + 'abc' + '.*', re.IGNORECASE)  # 匹配除换行符 \n 之外的任何单字符, 0次或多次
    res = collection.find({'content':rexExp })  
    for rs in res:  
        print(rs)

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))
