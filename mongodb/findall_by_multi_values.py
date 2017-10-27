import pymongo

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

    
    contents = collection.find(
            {"$and": [{"content": re.compile('.*abc.*', re.IGNORECASE)}, 
                      {"time": 
                          {'$gt': datetime.datetime(2017, 11, i, 0, 0, 0, 0),
                          '$lt': datetime.datetime(2017, 11, i+1, 0, 0, 0, 0)}
                      }]
            }
)
    for x in contents:
        print(x['sha1'])

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))
