from collections import deque

queue = deque([1,2])
queue.append(3)# push
queue.append(4)# push
queue.append(5)# push
x = queue.popleft()# pop
print(x)# 1
x = queue.popleft()# pop
print(x)# 2
x = queue.popleft()# pop
print(x)# 3
# current queue
print(queue)# [4,5]


