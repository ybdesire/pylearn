# run and reproduce the mongodb error
# RecursionError: maximum recursion depth exceeded in comparison

import bson

d = {}
d['key'] = d  # self-reference occurs
bson.BSON.encode(d)
# RecursionError: maximum recursion depth exceeded in comparison

# how to fix
# d['key'] = copy.deepcopy(d)
