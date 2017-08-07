import pymongo

host="10.20.30.40:27017"
dbname="db_name"
collname="collection_name"
username="user_name"
passwd="password"

client = pymongo.MongoClient(host)
client.the_database.authenticate(username, passwd, source=dbname)

db = client[dbname]
collection = db[collname]

searchmeta = {}
searchmeta["basic_info.product_name"]='xxx'

ret = collection.find_one(searchmeta)

print(ret)