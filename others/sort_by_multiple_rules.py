unsorted = [('b', 4, 2), ('b', 4, 3), ('b', 7, 3), ('b', 7, 2),('a', 4, 2, 3), ('a', 4, 2, 1), ('a', 4, 1, 2), ('a', 4, 1, 3)]
sorted(unsorted, key=lambda element: (element[0], element[1], element[2]))

```
[('a', 4, 1, 2),
 ('a', 4, 1, 3),
 ('a', 4, 2, 3),
 ('a', 4, 2, 1),
 ('b', 4, 2),
 ('b', 4, 3),
 ('b', 7, 2),
 ('b', 7, 3)]

```

