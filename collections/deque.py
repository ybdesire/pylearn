from collections import deque

# deque: list-like container with fast appends and pops on either end

d = deque('abc')
print(d) # deque(['a', 'b', 'c'])

d.append('d')
d.appendleft('e')
print(d)# deque(['e', 'a', 'b', 'c', 'd'])

r=d.pop()
print(r, d)# d deque(['e', 'a', 'b', 'c'])

r=d.popleft()
print(r, d)# e deque(['a', 'b', 'c'])

d = deque(reversed(d))
print(d)# deque(['c', 'b', 'a'])

