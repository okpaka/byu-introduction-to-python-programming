"""
this is an example of a while loop
"""

# initialize the variable
Number = int(input("Enter a positive number: "))

# check if the input is a not a negative number

while Number < 0:
    Number = input("Enter a positive number")
    Number = int(Number)
print("You entered a positive number ", Number)