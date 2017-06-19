d = {"a":4, "b":6, "c":2, "d":1, "e":3, "f":5, }
# sort by value and get key list
# descending order
l = sorted(d, key=d.get, reverse=True)

print(l)
