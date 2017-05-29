from pybloom import BloomFilter

f = BloomFilter(capacity=1000, error_rate=0.001)

[f.add(x) for x in range(10)]


print('20 in f: {0}'.format(20 in f))
print('3 in f: {0}'.format(3 in f))
