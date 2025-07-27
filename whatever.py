# Number Guessing Game


# Step 1 : Introductions

print(' ')
print('Welcome Player! You Will Be Guessing The Number I Chose')
print(' ')
print('Hint: Remember! The Numbers Will Only Range From 1 to 10')
print(' ')
print('Without A Further A Do, You May Begin, Goodluck!')
print(' ')


# Step 2: Python Chooses A Random Number

import random 

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
chosen_number = random.choice(numbers)



# Step 3: Ask Player To Guess

guess = input('Guess A Number Between 1 through 10:')
print(' ')

if guess == chosen_number:
    print('Congratulations!')
    print(' ')
    print('Game Has Ended')
else:
    print(' ')
    print('Oops, Wrong Guess')
    print(' ')
    print('Would You Like To Try Again?')
    print(' ')
    try_again = input("Type 'yes' or 'no': ")

    if try_again == 'yes':
        print(' ')
        guess = input("Guess Again: ")
        if guess == chosen_number:
            print("Congrats!")
            print(" ")
            print("Game Has Ended")
        else:
            print(f"Better Luck Next Time. The answer was {chosen_number}")
    else: 
        print(' ')
        print("Game Has Ended")
