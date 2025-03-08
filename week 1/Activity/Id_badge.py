#get the details of the user

FirstName = input("what is your first name? ")
LastName = input("what is your last name? ")
Email = input("what is your email address? ")
PhoneNumber = input("what is your phone number? ")
jobTitle = input("what is your job title? ")
IdNumber = input("what is your id number? ")

#convert the user's input to the desired format
LastName = LastName.upper()
Email=Email.lower()
jobTitle=jobTitle.capitalize()

#let's print the user's input along with conversion
print(f"Welcome to the ID badge generator")
print(f"The ID Card is:")
print(f"{LastName}, {FirstName}")
print(f"{jobTitle}")
print(f"ID: {IdNumber}")
#add empty space
print()
#print a line
print("--------------------")
#add empty space
print()
print(f"{Email}")
print(f"{PhoneNumber}")
print("--------------------")
