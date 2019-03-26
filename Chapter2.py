number = ''
import sys

while True:
    print('Please enter a number.')
    number = int(input())

    if number == '1':
        print('1, is the first number')
        continue
    if number == '2':
        print('2, is the second number')
        continue
    if number == '3':
        print('3, is the third number')
        continue
    if number == '4':
        print('4, is the fourth number')
        continue
    if number == 9:
        sys.exit()