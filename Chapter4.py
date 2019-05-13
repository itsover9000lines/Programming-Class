'''

Hunter O'Neill

v1

End of Line

4/29/19

This program has a set of 8 Avengers, the user running the program is asked to enter 8 villian
names, the program will randomly select an avenger, and a villian. It will randomly select the outcome,
the Avengers winning, or the villians.


'''

import random # imports the random module

avengers = ['Thor', 'Iron Man', 'Spiderman', 'Hulk', 'Falcon', 'Black Widow', 'Antman', 'Captain America']
verb = ['smashed', 'kicked', 'slapped', 'bonked']
villian = []
# these are the lists that the script will use

for i in range(8):
    villian.append(input('Enter villian number ' + str(i + 1))) # asks user to list 8 villians

print('Welcom to Avengers: End of Line!') # welcomes the user
input('Press "Enter" to continue.') # asks the user to press the enter key to continue the script

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

    selectedAvenger = random.choice(avengers) # selects a random avenger
    selectedVillian = random.choice(villian) # selects a random villian
    selectedVerb = random.choice(verb) # selects a random verb
    
    winner = []
    winner.append(selectedAvenger)
    winner.append(selectedVillian)
    
    loser = random.choice(winner) # selects a loser

    winner.remove(loser) # removes the loser from the winner list

    print(winner + ' ' + selectedVerb + ' ' +  loser) # prints the result

    if len(villian) <= 1:
        break
    
    if winner == [selectedAvenger]:
        villian.remove(selectedVillian)

    else: avengers.remove(selectedAvenger)
    # if the winner is the avengers, then the villian gets removed, and vice versa

if len(avengers) >= 2:
    print('The Avengers win! The surviving members are ')
    print(avengers)
else:
    print('The villians win! The surviving memebrs are ')
    print(villian)

# prints the final result