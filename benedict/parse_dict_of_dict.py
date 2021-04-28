# pip install python-benedict
# https://github.com/fabiocaccamo/python-benedict

from benedict import benedict

d = benedict({'dict1': {'foo': 1, 'bar': {'d3':3, 'd4':4, 'd5':{'a':'aaa', 'b':'bbb'}}}, 'dict2': {'baz': 3, 'quux': 4}})

def traverse_item(dct, key, value):
    print('key: {} - value: {}'.format(key, value))

d.traverse(traverse_item)




'''
key: dict1 - value: {'foo': 1, 'bar': {'d3': 3, 'd4': 4, 'd5': {'a': 'aaa', 'b': 'bbb'}}}
key: foo - value: 1
key: bar - value: {'d3': 3, 'd4': 4, 'd5': {'a': 'aaa', 'b': 'bbb'}}
key: d3 - value: 3
key: d4 - value: 4
key: d5 - value: {'a': 'aaa', 'b': 'bbb'}
key: a - value: aaa
key: b - value: bbb
key: dict2 - value: {'baz': 3, 'quux': 4}
key: baz - value: 3
key: quux - value: 4

'''


