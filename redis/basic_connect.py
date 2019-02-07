import redis #pip install redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)#connect to redis server
r.set('foo', 'bar')#set data
s = r.get('foo')#get data
print(s)