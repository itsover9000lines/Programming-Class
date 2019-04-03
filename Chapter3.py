def collatz(number): # defines collatz

    if number % 2 == 0: # if the number is even this runs
        print(number // 2)
        return number // 2

    elif number % 2 == 1: # if the number is odd this bit of code runs
        final = 3 * number + 1
        print(final)
        return final

num = input() # the number the user enters is stored as "num"
while num != 1: # if the number isn't at 1 it will keep looping
    num = collatz(int(num)) # this calls the function