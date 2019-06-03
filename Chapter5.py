'''

Hunter O'Neill

v2

End of Line

5/23/19

This program has a set of 8 Avengers, the user running the program is asked to enter 8 villain
names, and power levels. The program will randomly select an avenger, and a villain. It will select 
the outcome based on power and hitpoints. The Avengers winning, or the villains.


'''

import random
import pprint

avengers = {
    'Thor': {'power': 7, 'pts': 6},
    'Iron Man': {'power': 10, 'pts': 10},
    'Spiderman': {'power': 4, 'pts': 3},
    'Hulk': {'power': 6, 'pts': 5},
    'Falcon': {'power': 5, 'pts': 4},
    'Black Widow': {'power': 4, 'pts': 3},
    'Antman': {'power': 4, 'pts': 3},
    'Captain America': {'power': 6, 'pts': 5}
}

verb = [
    'smashed',
    'kicked',
    'slapped',
    'bonked'
    ]

villain = {}


for i in range(8):
    name = input('Enter villain name number ' + str(i + 1))
    try:
        power = int(input('Enter the villains power number'))
    except ValueError:
        print('Thats not a number! Please enter a number.')


    villain[name] = {'power': power, 'pts': 6}


pprint.pprint(villain)
pprint.pprint(avengers)


    
print('Welcom to Avengers: End of Line!')
input('Press "Enter" to continue.')

for keys in avengers:

    selectedAvenger = {}
    
    random.choice(avengers.items())

    print(selectedAvenger)

    selectedvillain = random.choice(list(villain))

    selectedVerb = random.choice(verb)
    # selects all the data used in the script ^

    print(avengerData)

    winner = []
    loser = []

    print(winner)
    print(loser)

    #print(winner[0] + ' ' + selectedVerb + ' ' +  loser)
    
    if winner == [selectedAvenger]:
        del villain[selectedvillain]

    else:
        del avengers[selectedAvenger]
    # if the winner is the avengers, then the villain gets removed, and vice versa

    if villain.keys() == 0:
        break

if len(avengers) >= 2:
    print('The Avengers win! The surviving members are ')
    print(avengers)
else:
    print('The villains win! The surviving memebrs are ')
    print(villain)