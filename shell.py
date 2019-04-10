# the >>> didnt copy and i really didnt feel like adding it to each line

[1, 2, 3]
[1, 2, 3]
['cat', 'bat', 'rat', 'elephant']
['cat', 'bat', 'rat', 'elephant']
['hello', 3.1415, True, None, 42]
['hello', 3.1415, True, None, 42]
spam = ['cat', 'bat', 'rat', 'elephant']
spam
['cat', 'bat', 'rat', 'elephant']


spam[0]
'cat'
spam[1]
'bat'
spam[2]
'rat'
spam[3]
'elephant'
['cat', 'bat', 'rat', 'elephant'][3]
'elephant'
'Hello ' + spam[0]
'Hello cat'
'The ' + spam[1] + ' ate the ' + spam[0] + '.'
'The bat ate the cat.'
spam[10000]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
spam[1]
'bat'
spam[1.0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not float
spam[int(1.0)]
'bat'



spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
['cat', 'bat']
spam[0][1]
'bat'
spam[1][4]
50



spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
'elephant'
spam[-3]
'bat'
'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
'The elephant is afraid of the bat.'
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4]
['cat', 'bat', 'rat', 'elephant']
spam[1:3]
['bat', 'rat']
spam[0:-1]
['cat', 'bat', 'rat']
spam[:2]
['cat', 'bat']
spam[1:]
['bat', 'rat', 'elephant']
spam[:]
['cat', 'bat', 'rat', 'elephant']
spam = ['cat', 'dog', 'moose']
len(spam)
3


spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam
['cat', 'aardvark', 'rat', 'elephant']
spam[2] = spam[1]
spam
['cat', 'aardvark', 'aardvark', 'elephant']



[1, 2, 3] + ['A', 'B', 'C']
[1, 2, 3, 'A', 'B', 'C']
['X', 'Y', 'Z'] * 3
['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
spam
[1, 2, 3, 'A', 'B', 'C']



spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam
['cat', 'bat', 'elephant']
del spam[2]
spam
['cat', 'bat']
