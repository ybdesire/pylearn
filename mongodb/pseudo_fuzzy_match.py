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

    rexExp = re.compile('.*', re.IGNORECASE)  # 匹配除换行符 \n 之外的任何单字符, 0次或多次
    res = collection.find({'content':rexExp })  # find all
    
    # then check by raw python logic
    for rs in res:  
        if('abc' in rs['content']):
            print(rs['sha1'])   

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))
