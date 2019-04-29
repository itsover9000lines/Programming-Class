'''

Hunter O'Neill
4/29/19

'''

import random # imports the random module

avengers = ['Thor', 'Iron Man', 'Spiderman', 'Hulk', 'Falcon', 'Black Widow', 'Antman', 'Captain America']
verb = ['smashed', 'kicked', 'slapped', 'bonked']
villian = []
# these are the lists that the script will use

for i in range(8):
    villian.append(input('Enter 8 villian names. (Villian number ' + str(i + 1) + ')')) # asks user to list 8 villians

print('Welcom to Avengers: End of Line!') # welcomes the user
input('Press "Enter" to continue.') # asks the user to press the enter key to continue the script

selectedAvenger = random.choice(avengers)
selectedVillian = random.choice(villian)
selectedVerb = random.choice(verb)

