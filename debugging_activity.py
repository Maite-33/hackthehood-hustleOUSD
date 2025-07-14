# Debugging Activity With Maite R.

# Code Snippet 1:
# Incorrect:

print(' ')
print("Case 1 ~~~~~~")
print(' ')

# Incorrect:
x = 10
y = 2
result = x / y
print("Result:", result)

# Problem: Division by zero, a number can not be devided by 0, it will come up as an error
# Solution: Change the value of y. For example, the number 2 instead of 0


# Code Snippet 2: 

print(' ')
print("Case 2 ~~~~~~")
print(' ')
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
   print(numbers[i])

# Encountered a logical error and runtime error: with [i+1] making out of range
# Solution: Deleted [i+1]. replaced it with just [i]


# Code Snippet 3:

print(' ')
print("Case 3 ~~~~~~")
print(' ')

def calculate_area(radius):
   area = 3.14 * radius ** 2
   return area
 
radius = 5
print(calculate_area(radius))

# Problem: Syntax Error, forgot the ':' at the end of def calculate_area(radius)
# Solution: Added a ":" (colon) at the end of the function to find the area


# Code Snippet 4:

print(' ')
print("Case 4 ~~~~~~")
print(' ')

def is_even(number):
   if number % 2 == 0:
       return True
   else:
       return False
 
print(is_even(4))
print(is_even(7))

print(' ')

# Problem: Syntax Error, no colon at the end of the if statement as well as at the end of else
# Solution: Add a colon at the end of the if statement and at else

# Code Snippet 5:

print("case 5 ~~~~~~")
print(' ')

for i in range(5):
   print(i)

# Problem: Syntax Error, an expetec colon at the end of for i in range(5)
# Solution: Add a colon at the end of the for loop command


# Code Snippet 6:

print(' ')
print('Case 6 ~~~~~~')
print(' ')

def greet(name):
   return "Hello, " + name
 
print(greet("Alice"))

# Problem: Syntax Error, it says that name is an invalid syntax
# Solution: Added a + inbetween return "Hello, " and name

# Code Snippet 7:

print(' ')
print('Case 7 ~~~~~~')
print(' ')

numbers = [1, 2, 3, 4, 5]
sum = 0
for number in numbers:
    sum += number
    print("Sum of numbers:", sum)

# Problem: Syntax Error: Invalid Indentation
# Solution: Put an indent block after the for statement, put it on line 86, sum += number as well as on the print statement


# Code Snippet 8:

print(' ')
print('Case 8 ~~~~~~')
print(' ')

def factorial(n):
   if n == 0:
       return 1
   else:
       return n * factorial(n-1)
 
print(factorial(5))

# Problem: Logical Error, factorial mulitplies the numbers before the original number
# Solution: instead of having factorial(n+1), it should be (n-1)


# Code Snippet 9:

print(' ')
print('Case 9 ~~~~~~')
print(' ')

name = input("Enter your name: ")
if name == "Alice" or name == "Bob":
   print("Hello, " + name)
else:
   print("Hello, stranger!")


# Problem: Logical Error? It does not print Hello Stranger if the name is other than Alice or Bob
# Solution: Add name == before Bob, so python can recognize it as an element too, so the else statement could work as well?


# Code Snippet 10:

print(' ')
print('Case 10 ~~~~~~')
print(' ')

def divide_numbers(x, y):
   result = x / y
   return result
 
num1 = 10
num2 = 2
print(divide_numbers(num1, num2))

# Problem: Division by Zero, a number can not be devided by 0.
# Solution: Change 0 into any other number