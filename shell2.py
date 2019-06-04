Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> spam = "That is Alice's cat."
>>> spam = 'Say hi to Bob\'s mother.'
>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
Hello there!
How are you?
I'm doing fine.
>>> print(r'That is Carol\'s cat.')
That is Carol\'s cat.
>>> spam = 'Hello world!'
>>> spam[0]
'H'
>>> spam[4]
'o'

>>> spam[-1]
'!'
>>> spam[0:5]
'Hello'
>>> spam[:5]
'Hello'
>>> spam[6:]
'world!'
>>> spam = 'Hello world!'
>>> fizz = spam[0:5]
>>> fizz
'Hello'
>>> 'Hello' in 'Hello World'
True
>>> 'Hello' in 'Hello'
True
>>> '' in 'spam'
True
>>> 'cats' not in 'cats and dogs'
False
>>> spam = 'Hello world!'
>>> spam = spam.upper()
>>> spam
'HELLO WORLD!'
>>> spam = spam.lower()
>>> spam
'hello world!'
>>> spam = 'Hello world!'
>>> spam.isLower()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    spam.isLower()
AttributeError: 'str' object has no attribute 'isLower'
>>> spam.islower()
False
>>> spam.isupper
<built-in method isupper of str object at 0x000001F33648BAB0>
>>> spam.isupper()
False
>>> 'HELLO'.isupper()
True
>>> 'abc12345'.islower()
True
>>> '12345'.islower()
False
>>> '12345'.isupper()
False
>>> 'Hello'.upper()
'HELLO'
>>> 'Hello'.upper().lower()
'hello'
>>> 'Hello'.upper().lower().lower()
'hello'
>>> 'Hello'.upper().lower().lower().upper()
'HELLO'
>>> 'HELLO'.lower()
'hello'
>>> 'HELLO'.lower().islower()
True
>>> 'hello'.isalpha()
True
>>> 'hello123'.isalpha()
False
>>> 'hello123'.isalnum()
True
>>> 'hello'.isalnum()
True
>>> '123'.isdecimal()
True
>>> ' '.isspace()
True
>>> 'This Is Title Case'.istitle()
True
>>> 'This Is Title Case 123'.istitle()
True
>>> 'This Is not Title Case 123'.istitle()
False
>>> 'This Is NOT Title Case Either'.istitle()
False
>>> 'Hello world!'.startswith('Hello')
True
>>> 
