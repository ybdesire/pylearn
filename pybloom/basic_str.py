from pybloom import BloomFilter

f = BloomFilter(capacity=1000, error_rate=0.001)

f.add('hello')
f.add('my')
f.add('world')
f.add('like')
f.add('sun')
f.add('son')


print('son in f: {0}'.format('son' in f))
print('hello in f: {0}'.format('hello' in f))
print('oh in f: {0}'.format('oh' in f))
