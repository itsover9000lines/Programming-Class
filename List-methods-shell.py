spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')
0
spam.index('heyas')
3
spam.index('howdy howdy howdy')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 'howdy howdy howdy' is not in list
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
spam.index('Pooka')
1
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam
['cat', 'dog', 'bat', 'moose']
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam
['cat', 'chicken', 'dog', 'bat']
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam
['cat', 'rat', 'elephant']
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('chicken')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat')
spam
['bat', 'rat', 'cat', 'hat', 'cat']
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam
[-7, 1, 2, 3.14, 5]
spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam
['ants', 'badgers', 'cats', 'dogs', 'elephants']
spam.sort(reverse=True)
spam
['elephants', 'dogs', 'cats', 'badgers', 'ants']

spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam
['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam
['a', 'A', 'z', 'Z']

