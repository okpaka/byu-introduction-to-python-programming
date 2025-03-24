"""
 this program simulates a a child asking for candy from a parent
"""

Answer = input("Can I have some candy? (yes or no): ")
Answer = Answer.lower()

while Answer == "no":
    Answer = input("Can I have some candy? (yes or no): ")
    Answer = Answer.lower()
print("Thank you!")