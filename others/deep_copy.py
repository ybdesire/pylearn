import copy

d={1:1,2:2}

d3 = copy.deepcopy(d)
d3[1]=5

d2 = d
d2[1]=3



print('d2={0}'.format(d2))
print('d3={0}'.format(d3))
print('d={0}'.format(d))
