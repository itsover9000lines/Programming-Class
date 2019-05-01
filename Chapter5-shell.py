
>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
>>> myCat['size']
'fat'
>>> 'My cat has ' + myCat['color'] + ' fur.'
'My cat has gray fur.'
>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}
>>> spam = ['cats', 'dogs', 'moose']
>>> bacon = ['dogs', 'moose', 'cats']
>>> spam == bacon
False
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> eggs == ham
True
>>> spam = {'name': 'Zophie', 'age': 7}
>>> spam['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'color'
>>>
>>> spam = {'color': 'red', 'age': 42}
>>> for v in spam.values():
...         print(v)
... 
red
42
>>> for k in spam.keys():
...         print(k)
... 
color
age
>>> for i in spam.items():
...         print(i)
... 
('color', 'red')
('age', 42)
>>> spam = {'color': 'red', 'age': 42}
>>> spam.keys()
dict_keys(['color', 'age'])
>>> list(spam.keys())
['color', 'age']
>>> spam = {'color': 'red', 'age': 42}
>>> for k, v in spam.items():
...         print('Key: ' + k + ' Value: ' + str(v))
... 
Key: color Value: red
Key: age Value: 42
>>> spam = {'name': 'Zophie', 'age': 7}
>>> 'name' in spam.keys()
True
>>> 'Zophie' in spam.values()
True
>>> 'color' in spam.keys()
False
>>> 'color' not in spam.keys()
True
>>> 'color' in spam
False
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
'I am bringing 2 cups.'
>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
'I am bringing 0 eggs.'
>>> picnicItems = {'apples': 5, 'cups': 2}
>>> 'I am bringing ' + str(picnicItems['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'eggs'
>>> spam = {'name': 'Pooka', 'age': 5}
>>> spam.setdefault('color', 'black')
'black'
>>> spam
{'name': 'Pooka', 'age': 5, 'color': 'black'}
>>> 