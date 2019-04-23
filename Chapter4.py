import random

avengers = ['Thor', 'Iron Man', 'Spiderman', 'Hulk', 'Falcon', 'Black Widow', 'Antman', 'Captain America']
verb = ['smashed', 'kicked', 'slapped']
villian = []

print('Please enter 8 villian names')
while True:
    name = input()
    if name == '':
        print('Please enter a name')