# -*- coding: utf-8 -*-
from collections import defaultdict

members = [
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]

result = defaultdict(list)

for sex, name in members:
    result[sex].append(name)# no error here if sex not in the defaultdict

print(result)

'''
defaultdict(<class 'list'>, {'male': ['John', 'Jack', 'Pony'], 'female': ['Lily', 'Lucy']})
'''