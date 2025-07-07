# Step 1: Cat Function

def cat_greeting(word):
    print(f"Cat says {word}")

cat_greeting("Meow")

# Step 2: Superhero Power Function

def generate_superhero_power():
    name = "Anx"
    print(f"OH HO HO, YALL LOOK, {name}'s POWER IS TELEKINESIS!")

generate_superhero_power()

# Step 3: Superhero Power Function with Return

def generate_superhero_power1():
    power = "Telepathy"
    return power

# Step 4: Superhero Power Function with Arguments

def generate_superhero_power2(user_name, super_power):
    message = user_name + " has the power of "  + super_power + "!"
    return message
print(generate_superhero_power2("Sol", "flying"))

# Step 5: Looping Through Greetings

def cat_greetings_loop(greeting):
    for i in range(5):
        print(f"Aw look, the cat says {greeting}!")

cat_greetings_loop("meow")

# Step 6: Superhero Power Function With Multiple Powers

def generate_multiple_powers(powers):
    for i in powers:
        print(i)
print(' ')
print('List Of Super Powers???:')
print(' ')
list_of_powers = "Flying", "Invisibility", 'Super Strength', 'Telekinesis', 'Telepathy', 'Immortality', 'Time Travel', 
generate_multiple_powers(list_of_powers)

user_input = input("Would you like to see villain powers??? yes or no?")
if user_input == "yes":
    print(' ')
    print("VILLAIN POWERS:")
    print(' ')
    print("Mind Control")
    print(' ')
    print('Omniscience') 
    print(' ')
    print('Shapeshifting')
    print(' ') 
    print('Dark Magic')
    print(' ') 
    print('Absorption')
else:
    print("Alrighty, I guess you're not curious enough, dang.")





