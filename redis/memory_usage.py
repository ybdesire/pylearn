import redis #pip install redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)#connect to redis server
mem_used = r.info()['used_memory']
print(mem_used)# 854184, is 854k