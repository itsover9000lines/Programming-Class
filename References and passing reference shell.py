spam = 42
cheese = spam
spam = 100
spam
100
cheese
42
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello!'
spam
[0, 'Hello!', 2, 3, 4, 5]
cheese
[0, 'Hello!', 2, 3, 4, 5]

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam
['A', 'B', 'C', 'D']
cheese
['A', 42, 'C', 'D']
