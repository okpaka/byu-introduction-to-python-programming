"""
Your assignment is to write a program that asks the user for a temperature and then shows
the wind chill values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles 
per hour, just like the National Weather Service chart does.
To help users who are more familiarwith Celsius, your program 
should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, 
convert the Celsius temperature to Fahrenheit before using the formula."""

# The formula for wind chill is:
# W = 35.74 + 0.6215T - 35.75V^0.16 + 0.4275TV^0.16
# Where:
# W = wind chill in Fahrenheit
# T = temperature in Fahrenheit
# V = wind speed in miles per hour

# The formula for converting Celsius to Fahrenheit is:
# F = C * 9/5 + 32
# Where:
# F = temperature in Fahrenheit
# C = temperature in Celsius

# The formula for converting Fahrenheit to Celsius is:
# C = (F - 32) * 5/9
# Where:
# C = temperature in Celsius
# F = temperature in Fahrenheit

"""
define a function and return it's value
"""
def wind_chill(temp, wind_speed):
    """
    Calculate the wind chill using the formula:
    W = 35.74 + 0.6215T - 35.75V^0.16 + 0.4275TV^0.16
    """
    return 35.74 + (0.6215 * temp) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp * (wind_speed ** 0.16))

#prompt user for input
#display a menu
choice = ""

while choice != 3:
    print("Menu:")
    print("1. Calculate wind chill in Fahrenheit")
    print("2. Calculate wind chill in Celsius")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    if choice == 3:
        print("Exiting the program.")
        exit()
    elif choice == 1:
        temp = float(input("Enter the temperature in Fahrenheit: "))
        wind_speed = float(input("Enter the wind speed in miles per hour: "))
        wind_chill_value = wind_chill(temp, wind_speed)
        print(f"The wind chill is: {wind_chill_value} °F")
    elif choice == 2:
        temp_celsius = float(input("Enter the temperature in Celsius: "))
        temp_fahrenheit = (temp_celsius * 9/5) + 32
        wind_speed = float(input("Enter the wind speed in miles per hour: "))
        wind_chill_value = wind_chill(temp_fahrenheit, wind_speed)
        print(f"The wind chill is: {wind_chill_value} °F")