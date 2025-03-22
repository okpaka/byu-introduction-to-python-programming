# This program calculates the price of a meal, 
""" 
Author: Okpaka Lucky Great
Date: 2025 March 8

"""


# The price of the meal is stored in the variable meal_price
child_meal_price = float(input("Enter the price of a child's meal: "))
adult_meal_price = float(input("Enter the price of a adult's meal: "))
num_of_children = int(input("Enter the number of children: "))
num_of_adults = int(input("Enter the number of adults: ") )


# perform sub_total calculation and display the result
children_total = num_of_children * child_meal_price
adult_total = num_of_adults * adult_meal_price

sub_total = children_total + adult_total

print(f"subtotal: ${sub_total}")

# Ask user and display the tax amount
sales_tax_rate = float(input("Enter the sales tax rate: "))
tax_amount = sales_tax_rate/100 * sub_total

print(f"Sales Tax: ${tax_amount}")
print(f"Total: {sub_total + tax_amount}")

Payment = float(input("Enter the amount paid: "))
change = Payment - (sub_total + tax_amount)
print(f"Change: ${change}")
