# Lab 3

# Task 1: Working with Strings 
food = "Carne Asada"

print(food[0:3]) #Print first 3 characters
print(food[-3:]) #Print last 3 characters

first_last = food[0] + food[-1] #combine first and last character
print(first_last)

food_list = food.split()

print(food_list)
joined_food = " " .join(food_list)
print(joined_food)


# Task 2: Working with Lists
number_lists = [3, 6, 9, 12, 15, 18]

number_lists.append(0)
print(number_lists)

number_lists.insert(3, 1000)
print(number_lists)

number_lists.pop()
print(number_lists)

number_lists.remove(number_lists[1])
print(number_lists)

print(number_lists[:3])
print(number_lists[-3:])


# Task 3: Working With Dictionaries

books = {"Jeff Kinney": 'The Diary of The Wimpy kid',
        'Manohar Malgonkar': ' Bend in the Ganges',
        'Ashok Gupta': 'A Billion Is Enough',
        'Toni Morrison': 'Beloved'}
print(books.keys())
print(books.values())
print(books.get())

books.pop('Toni Morrison')
print(books)

del books['Jeff Kinney']
print(books)
