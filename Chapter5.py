'''

Hunter O'Neill

v2

End of Line

5/23/19

This program has a set of 8 Avengers, the user running the program is asked to enter 8 villian
names, and power levels. The program will randomly select an avenger, and a villian. It will select 
the outcome based on power and hitpoints. The Avengers winning, or the villians.


'''

import random

avengers = {
    'Thor': {'power': 7, 'Pts': 6},
    'Iron Man': {'power': 10, 'Pts': 10},
    'Spiderman': {'power': 4, 'Pts': 3},
    'Hulk': {'power': 6, 'Pts': 5},
    'Falcon': {'power': 5, 'Pts': 4},
    'Black Widow': {'power': 4, 'Pts': 3},
    'Antman': {'power': 4, 'Pts': 3},
    'Captain America': {'power': 6, 'Pts': 5}
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
    try:
        power = int(input('Enter the villains power number'))
    except ValueError:
        print('Thats not a number! Please enter a number.')


    villian[name] = {'power': power, 'Pts': 6}


print(villian)
print(avengers)


    
print('Welcom to Avengers: End of Line!')
input('Press "Enter" to continue.')

for keys in avengers:

    selectedAvenger = random.choice(list(avengers.keys()))
    selectedVillian = random.choice(list(villian.keys()))
    selectedVerb = random.choice(verb)

    winner = []
    winner.append(selectedAvenger)
    winner.append(selectedVillian)
    
    loser = []

    

    print(winner[0] + ' ' + selectedVerb + ' ' +  loser)
    
    if winner == [selectedAvenger]:
        del villian[selectedVillian]

    else:
        del avengers[selectedAvenger]
    # if the winner is the avengers, then the villian gets removed, and vice versa

    if len(villian) == 0:
        break

if len(avengers) >= 2:
    print('The Avengers win! The surviving members are ')
    print(avengers)
else:
    print('The villians win! The surviving memebrs are ')
    print(villian)