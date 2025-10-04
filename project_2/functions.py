# Define a function names circle_calculations that:
    # Takes the radius of a circle as input.
    # Returns both the circumference and area of the circle
# Asks the user to input the radius 
# Calls the function and prints the results
# Us the formula for circumference 2 * pi * radius and area pi * radius^2.
# Use the math module for pi

# Ex:
    # Enter the radius of the circle: 3
    # For a circle with radius 3:
        # When printing the Circumference and the Area, the example is showing 14 decimal places.
    # Circumference = 18.849...
    # Area = 28.274...

# Importing math module
import math

# Define the function
def circle_calculations(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return circumference, area

# Ask user for input
radius = float(input("Enter the radius of the circle: "))

# Calling function
circumference, area = circle_calculations(radius)

print(f"For a circle with radius {radius}")
print(f"Circumference = {circumference}")
print(f"Area = {area}")