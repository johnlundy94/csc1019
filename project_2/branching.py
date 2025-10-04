# Ask the user to input a number
# Checks if the number is
    # Positive, negative, or zero
    # Even or odd
# Print appropriate messages for each case

# Ex
    # Enter a number: 7
    # The number 7 is positive
    # The number 7 is odd

# Get user input
num = int(input("Enter a number: "))

# Checking if the number is positive, negative or zero
if num > 0:
    print(f"The number {num} is positive")
elif num < 0:
    print(f"The number {num} is negative")
else:
    print(f"The number {num} is zero")

# Checking if number is odd or even
if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")

