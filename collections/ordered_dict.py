import collections


print('basic dict, output may no order') 
d={}  
d['a']='A'  
d['b']='B'  
d['c']='C'  
for k in d:
    v = d[k]
    print(k,v)


print('basic dict, output order the same as input order')   
d=collections.OrderedDict()  
d['a']='A'  
d['b']='B'  
d['c']='C'  
for k in d:
    v = d[k]
    print(k,v)

print('current d: {0}'.format(d))
d.move_to_end('a')
print('now d: {0}'.format(d))

'''

basic dict, output may no order
a A
c C
b B
basic dict, output order the same as input order
a A
b B
c C

current d: OrderedDict([('a', 'A'), ('b', 'B'), ('c', 'C')])
now d: OrderedDict([('b', 'B'), ('c', 'C'), ('a', 'A')])
'''