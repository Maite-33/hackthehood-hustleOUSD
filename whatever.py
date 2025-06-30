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

guess = input('Guess A Number Between 1 through 10')

if guess == chosen_number:
    (print('Congratulations!'))
#else:
    #print(f'Oops, Wrong Guess. The correct answer was {chosen_number}') #maybe i could add that else: oops wrong guess. and then ask the player "This is your last chance
                                                                        #do you want to try again, yes or no?" if the player says no, stop the program, and the player says yes
                                                                        #let them guess again, and if they get it wrong show the right answer, and if get it right, show "congrats!"


print('Oops, Wrong Guess. Would You Like To Try Again? Yes or No?')

guess: ("yes", 'no')
if guess == 'yes':
    print('Guess A Number Again')
