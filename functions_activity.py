# Step 1
menu = {'Pizza': 2.99, 'Burger': 3.99, 'Hot dog': 1.99, 'Cheese': 0.59, 'Ice cream': 1.49, 'Churro': 0.79, 'Soda': 0.89}

# Step 2
def total_price(item1, item2):
    total_sum = menu.get(item1) + menu.get(item2)
    return total_sum

print (total_price('Pizza', 'Burger'))

# Step 3

def price_difference(item1, item2):
    total_difference = abs(menu[item1] - menu[item2])
    return total_difference

print(price_difference('Hot dog', 'Burger'))

# Step 4

def inflation(item, number):
    new_price = menu.get(item) * number
    menu[item] = new_price
    return menu
print(inflation('Churro', 4))


# Step 5

def deflation(item, number):
    new_price = menu.get(item) / number
    menu[item] = new_price
    return menu
print(deflation('Churro', 4))

# Step 6

def pay_and_get_change(item1, item2, money_given):
    total_sum = menu[item1] + menu[item2]
    change = money_given - total_sum
    if money_given < total_sum:
        return "Not enough money"
    else:
        return change

print(pay_and_get_change('Pizza', 'Burger', 5))

#or the change after paying, in case the person has a bill of 10 or any other bill, it would be the bill - item cost, to throw out the change. 