option=input("COLLEGE or HIGH SCHOOL: ")

if option == "COLLEGE":
#college
    field = input("Enter your field of study: ")
    if field == "Engineering":
        print("Welcome to College of Engineering")
    elif field == "Science":
        print("Welcome to College of Science")
    elif field == "Art":
        print("Welcome to College of Art")
    else:
        print("Welcome to College")

#high school
elif option == "HIGH SCHOOL":
    subject = input("Enter your subject: ")
    if subject == "Mathematics":
        print("Welcome to High School of Mathematics")
    elif subject == "Science":
        print("Welcome to High School of Science")
    elif subject == "Art":
        print("Welcome to High School of Art")
    else:
        print("Welcome to High School")
else:
    print("Invalid option")
