import ast


'''
objective: convert string to it's own type data format
'''
s1 = u'[1,2,3]'
s2 = '[1,2,3]'
s3 = '[{1:11},{2:22},{3:33}]'


s1t = ast.literal_eval(s1)
s2t = ast.literal_eval(s2)
s3t = ast.literal_eval(s3)


print('s1 type = {0}'.format(type(s1)))
print('s1_eval type = {0}'.format(type(s1t)))
print('s1 element value = {0}'.format(s1t[0]))

print('s2 type = {0}'.format(type(s2)))
print('s2_eval type = {0}'.format(type(s2t)))
print('s2 element value = {0}'.format(s2t[0]))

print('s3 type = {0}'.format(type(s3)))
print('s3_eval type = {0}'.format(type(s3t)))
print('s3 element value = {0}'.format(s3t[0]))



