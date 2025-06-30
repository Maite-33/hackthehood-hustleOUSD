# Task 1: checking Voting Eligibility Repeatedly 

checking = 'yes'

while checking == 'yes':
    print('What is your age?')
    user_input = input()
    if int(user_input) >= 18:
        print("Of course! You are eligible to vote!")
    else:
        print('Aw shucks, you arent eligle to vote just yet!')
    print("Would you like to check another age? yes or no?")
    user_input2 = input()
    checking = user_input2


# Task 2: Checking Multiple Numbers for Positivity or Negativity

list1 = (3, -1, 0, 6, -4)

for x in list1: 
    if x > 0:
        print("Value is positive!")
    elif x < 0:
        print("Value is negative!")
    else: 
        print("Number is zero!")


# Task 3: Collecting Blocks In Minecraft

inventory = ['tnt', 'glass', 'grass', 'netherite', 'waxed lightly weathered chiseled copper stairs']


for i in inventory:
    if i == "netherite":
        print(f"OMGGG, CONGRATS, you got {i}!")
    else:
        print(f"Oh, look at you, you got {i}")

    