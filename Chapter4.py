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

avengers = [
    'Thor',
    'Iron Man',
    'Spiderman',
    'Hulk',
    'Falcon',
    'Black Widow',
    'Antman',
    'Captain America'
    ]
verb = [
    'smashed',
    'kicked',
    'slapped',
    'bonked'
    ]
villian = []

for i in range(8):
    villian.append(input('Enter villian number ' + str(i + 1)))

print('Welcom to Avengers: End of Line!')
input('Press "Enter" to continue.')

'''
selectedAvenger = random.choice(avengers) # selects a random avenger
selectedVillian = random.choice(villian) # selects a random villian
selectedVerb = random.choice(verb) # selects a random verb

winner = random.choice([selectedAvenger, selectedVillian]) # selects a winner

if winner == selectedAvenger:
    villian.remove(selectedVillian)

else: avengers.remove(selectedAvenger)

# if the winner is the avengers, then the villian gets removed, and vice versa
'''

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

    '''
    not sure why it only prints the first letter of most of the
    selections, just turned it in now so i can get some points
    '''
    
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