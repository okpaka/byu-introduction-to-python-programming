"""
Write functions to compute and return the areas of squares, rectangles, and circles. T
hese functions should not display the values directly, but rather should return them, 
so they could be used in other parts of the program.
"""
import math
def compute_area_square(side_length):
    """
    Calculate the area of a square given the length of its side.
    
    :param side_length: Length of the side of the square
    :return: Area of the square
    """
    return side_length ** 2

def compute_area_rectangle(length, width):
    """
    Calculate the area of a rectangle given its length and width.
    
    :param length: Length of the rectangle
    :param width: Width of the rectangle
    :return: Area of the rectangle
    """
    return length * width
def compute_area_circle(radius):
    """
    Calculate the area of a circle given its radius.
    
    :param radius: Radius of the circle
    :return: Area of the circle
    """

    return math.pi * (radius ** 2)

# Test the functions
#prompt user for input for a square
#display a menu


choice = ""
while choice != 4:
    print("Menu:")
    print("1. Calculate the area of a square")
    print("2. Calculate the area of a rectangle")
    print("3. Calculate the area of a circle")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 4:
        print("Exiting the program.")
        exit()
    elif choice == 1:
        side_length = float(input("Enter the length of the side of the square: "))
        area_square = compute_area_square(side_length)
        print(f"The area of the square is: {area_square}")
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area_rectangle = compute_area_rectangle(length, width)
        print(f"The area of the rectangle is: {area_rectangle}")
    elif choice == 3:
        radius = float(input("Enter the radius of the circle: "))
        area_circle = compute_area_circle(radius)
        print(f"The area of the circle is: {area_circle}")