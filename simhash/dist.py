from simhash import Simhash
# https://leons.im/posts/a-python-implementation-of-simhash-algorithm/

simhash1 = Simhash("This is a sample text to hash.")
simhash2 = Simhash("This is a sample text666 to hash666.")
print(simhash1.distance(simhash2)) # 16


