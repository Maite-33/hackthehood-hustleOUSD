# Guessing Game - Maite(Me) - Louis - Selina - Jayla


import random      # Import Random allows you to use the random module. Without it, it will return as an error

def generate_random_number():          # This function allows for a random number from 1 to 100 to be chosen
    return random.randint(1, 100)       # This returns a random integer in a specific range

def get_user_guess():            # Organizing and naming when defining a function
      
         
    while True:                  # Any coding under the while True will continue repeatedly to work until it reaches a stopping point (break)
        try:
            
            user_guess = int(input("Please Enter A Number Between (1-100): "))    # This allows for the user to put an answer to the words written inside the string. The int converts the input into an integer
            if 1<= (user_guess) <= 100:           # If the user guess is greater than or equal to and less than or equal to 100 
                return user_guess                 # it returns the user guess
            else:                                 # Other than that
                print("Enter A Valid Number ")    # If the user_guess is not a number, the computer will show "Enter A Valid Number" to the user

        except ValueError:                        # In other occasions, if the value number isn't entered and something else is entered
            print("This is not a number")         # it will return "This is not a number" back to the user


def play_guessing_game(): 
    secret_number = generate_random_number()     # Calling back to generate_random_number, it is now named as secret_number for organization

    print(' ')                                                                             # When running python, the words in the string will print and show to the user 
    print("welcome to the guessing game!")                                                 #
    print(' ')                                                                             #
    print("I'm thinking of a number, do you think have what it takes? Let's get started!") #
    print(' ')
    attempts = 0      # The attemps made will always equal to 0 once the game begins

    while True:                    # The condition will keep repeating until it is exited
        guess = get_user_guess()   # get_user_guess is renamed as guess for organization
        attempts += 1              # After each guess, attempts made will increase by one

        print(' ')
        print(f"Attempts Made : {attempts}") #It prints how many attempts made to show the user
        if guess < secret_number:                       # When the users guess also known as guess is less than the secret numer
            print("Oh wow, that's too low! Try again.") # Python will print "Oh wow, that's too low! Try again."

        elif guess > secret_number:                          # If the guess is not less than the secret number, but now it is greater than the secret number
            print("Woah there, that's too high! Try again.") # It will print "Woah there, that's too high! Try again."

        else:                                              # If the guess isn't greater than or less than the secret number, but IS the ceret number 
            print("Hoorayyy!! You got it! Congrats!")      # Python will print "Hoorayyy!! You got it! Congrats!"
            break                                          # To exit out of the while True, use break
    

def game_loop():                
    while True:                 # The conditions will continue to run and turn to True 
        play_guessing_game()     # This will initiate the game itself 
        user_input = input("Would You Like To Continue?").lower()   # Once the user is correectly guessed the number, python will print the string to the user, asking if they would coninue
        if user_input == 'yes':                                     # If the user says yes to continue, 
            play_guessing_game()                                    # the game will continue
        else:                                                       # If anything else other than yes is entered,
            print("Aw shucks, We'll see you next time!")            # python will print what's inside the string
            break                                                   # then finally exit out of the code, ending the game


# Had to search this one up, I don't know exactly what this is

if __name__ == "__main__":     # Using this, the coding underneath it will only work once it is called using its assigned file name
    game_loop()                # then it will initiate game_loop, whether it continues or not based on the users input 