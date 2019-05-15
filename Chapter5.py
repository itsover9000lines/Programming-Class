'''

Hunter O'Neill

v1

End of Line

4/29/19

This program has a set of 8 Avengers, the user running the program is asked to enter 8 villian
names, the program will randomly select an avenger, and a villian. It will randomly select the outcome,
the Avengers winning, or the villians.


'''

import random
from collections import defaultdict

avengers = {
    'name': 'Thor', 'power': 7,
    'name': 'Iron Man', 'power': 10,
    'name': 'Spiderman', 'power': 4,
    'name': 'Hulk', 'power': 6,
    'name': 'Falcon', 'power': 5,
    'name': 'Black Widow', 'power': 4,
    'name': 'Antman', 'power': 4,
    'name': 'Captain America', 'power': 6
    }
verb = [
    'smashed',
    'kicked',
    'slapped',
    'bonked'
    ]

villian = {}


for i in range(8):
    name = input('Enter villian name number ' + str(i + 1))
    power = input('Enter the villains power number')

    villian[name]=power


print(villian)


    
'''
print('Welcom to Avengers: End of Line!')
input('Press "Enter" to continue.')

while len(avengers) >= 1:

    selectedAvenger = random.choice(avengers)
    selectedVillian = random.choice(villian)
    selectedVerb = random.choice(verb)
    
    winner = []
    winner.append(selectedAvenger)
    winner.append(selectedVillian)
    
    loser = random.choice(winner)

    winner.remove(loser)

    print(winner[0] + ' ' + selectedVerb[0] + ' ' +  loser[0])
    
    if winner == [selectedAvenger]:
        villian.remove(selectedVillian)

    else:
        avengers.remove(selectedAvenger)
    # if the winner is the avengers, then the villian gets removed, and vice versa

    if len(villian) == 0:
        break

if len(avengers) >= 2:
    print('The Avengers win! The surviving members are ')
    print(avengers)
    print(villian)
else:
    print('The villians win! The surviving memebrs are ')
    print(villian)
    print(avengers)
'''