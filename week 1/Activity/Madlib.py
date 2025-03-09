"""
Prints out a madlib with the following words filled in:
NOUN, ADJECTIVE, VERB, NOUN

Author: Okpaka Lucky
Date: 2025 march 7

I have added a review option to the madlib game
"""
#create a variable for each word
Noun = input("Enter a NOUN: ")
Adjective = input("Enter an ADJECTIVE: ")  
Verb = input("Enter a VERB: ")
Noun2 = input("Enter another NOUN: ")
exclamation = "hooray!".capitalize()


review = input("-----------------------Do you want to review your story? (yes/no): -----------------------")
if review == "yes":
    print("Your Story is: ")
    print("The other day, I was really in trouble. It all started when I saw a very "+ Adjective +" " + Noun + " "+ Verb+ " down the hallway. "+ exclamation +" I yelled. But all I could think to do was to " + Verb + " over and over. Miraculously, that caused it to stop, but not before it tried to drive right in front of my " + Noun2)
else:
    print("Thank you for playing the game")