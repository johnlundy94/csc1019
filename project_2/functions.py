# Algorithm:
# 1. Define a function named circle_calculations that:
#       - Takes the radius of a circle as input.
#       - Returns both the circumference and area of the circle.
# 2. Ask the user to input the radius.
# 3. Call the circle_calculations function.
# 4. Display the circumference and area of the circle using the returned values.
# 5. Use the math module for the constant pi in calculations.

# Pseudocode:
# BEGIN
#     IMPORT math module
#     DEFINE function circle_calculations(radius)
#         SET circumference = 2 * math.pi * radius
#         SET area = math.pi * radius^2
#         RETURN circumference, area
#     END FUNCTION
#
#     PROMPT user to enter radius
#     CALL circle_calculations(radius)
#     DISPLAY "For a circle with radius", radius
#     DISPLAY "Circumference =", circumference
#     DISPLAY "Area =", area
# END

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