from diskcache import Cache
# http://www.grantjenks.com/docs/diskcache/tutorial.html


# 1. set & save
cache = Cache("cachedir")# save to this dir
cache.set('key', 'value')# set
cache.close()# close


# 2. get
del cache
cache = Cache("cachedir")# save to this dir
v = cache['key']
print(v)

