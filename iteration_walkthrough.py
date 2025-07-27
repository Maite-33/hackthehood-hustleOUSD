# Hustle OUSD - ParkerBroadcast

# Tiger Teams lists

yellow = ['Sebastian', 'Erika', 'Emari', 'Jessie', 'Kwarme', 'Juan', 'Azhar', 'Kalen', 'Taur', 'Vincent', 'Amori']

# Check roster function

def roster(name, yellow):
    #i = 0
    for i in range(11):
        if(name == yellow[i]):
            return True
        

        i =+ 1

    return False

    def roster_check(name):
        #counter = 0
        while(counter < 10):
            print(yellow[counter])
            print(name)

            i =+ 1

    #i = 0
    #for i in range(11):
        #print(yellow[i])
        #i =+ 1
    
    #print(name)

    #return 0

# Main function
#roster('Kwarme', yellow)
name = "Kwarme"
#print(f"The student {name} is in the roster: {roster("Kwarme", yellow)}")
roster_check()


#so like i couldnt follow along cause the screen share froze sadly, okay nevermind. The issue was the indentation and the  on line 11, with the range(11)
