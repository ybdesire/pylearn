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

    
    contents = collection.find({'sha1':'''{0}'''.format('001')})
    
    for x in contents:
        print(x['sha1'])

except Exception as e:
    s = sys.exc_info()
    print('exception error msg : {0}'.format(s[1]))
    print('exception on line: {0} '.format(s[2].tb_lineno))
