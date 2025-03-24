"""
this is a text based adventure game that asks the user to choose between college and high school
and then asks the user to enter their field of study or subject respectively
then ask for each subject grade and then gives a feedback based on the grade entered

it is a simple game that helps the user to know if they can pursue a career in the field they entered
"""


option=input("COLLEGE or HIGH SCHOOL: ")
option = option.upper()
if option == "COLLEGE":
#college
    field = input("Enter your field of study: ")

    #Engineering
    if field == "Engineering":
        grade = int(input("Enter your grade: "))
        if grade > 70:
            print("You can pursue a career in Engineering")
        else:
            print("You need to improve your grades to pursue a career in Engineering")

    #Science
    elif field == "Science":
        grade = int(input("Enter your grade: "))
        if grade > 70:
            print("You can pursue a career in Science")
        else:
            print("You need to improve your grades to pursue a career in Science")

    #Art
    elif field == "Art":
        grade = int(input("Enter your grade: "))
        if grade > 70:
            print("You can pursue a career in Art")
        else:
            print("You need to improve your grades to pursue a career in Art")
    else:
        print("No career path for you for the field you entered")

#high school
elif option == "HIGH SCHOOL":
    subject = input("Enter your subject: ")

             #mathematics
    if subject == "Mathematics":
        print("Welcome to High School of Mathematics")
        if subject == "Mathematics":
            grade = int(input("Enter your grade: "))
            if grade > 70:
                print("You can pursue a career in Mathematics")
            else:
                print("You need to improve your grades to pursue a career in Mathematics")

            #Biology
    elif subject == "Biology":
            grade = int(input("Enter your grade: "))
            if grade > 70:
                print("You can pursue a career in Biology")
            else:
                print("You need to improve your grades to pursue a career in Biology")

            #Business studies
    elif subject == "Business studies":
            grade = int(input("Enter your grade: "))
            if grade > 70:
                print("You can pursue a career in Business studies")
            else:
                print("You need to improve your grades to pursue a career in Business studies")
                
    else:
        print("No career path for you for the subject you entered")
else:
    print("Invalid option")
