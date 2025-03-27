"""
t
"""

import random

Random_number = random.randint(1, 50)

user_guess = input("guess the word")
count = 1

    #validate less than
while int(user_guess) < Random_number or int(user_guess) > Random_number:
    if int(user_guess) > Random_number:
        user_guess = input("GREATER: try again")
        count += 1
    else :
        user_guess = input("LESS: try again")
        count += 1

if int(user_guess) ==  Random_number:
        print("you've guess correctly")
        print(f"you've guessed {count} times")