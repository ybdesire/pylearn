import pymongo,datetime

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

    
    sha1_list = collection.distinct(
    'sha1',
    { 
        'time': {
            '$gt': datetime.datetime(2013, 10, 30, 0, 0, 0, 0),     # great than this date
            '$lt': datetime.datetime(2018, 05, 9, 0, 0, 0, 0)       # less than this date
        }
    })

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))
