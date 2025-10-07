# Algorithm:
# 1. Ask the user to enter a number.
# 2. Check if the number is positive, negative, or zero.
# 3. Display a message describing whether it is positive, negative, or zero.
# 4. Check if the number is even or odd.
# 5. Display a message describing whether it is even or odd.

# Pseudocode:
# BEGIN
#     PROMPT user for a number
#     IF number > 0 THEN
#         DISPLAY "The number is positive"
#     ELSE IF number < 0 THEN
#         DISPLAY "The number is negative"
#     ELSE
#         DISPLAY "The number is zero"
#     END IF

#     IF number MOD 2 == 0 THEN
#         DISPLAY "The number is even"
#     ELSE
#         DISPLAY "The number is odd"
#     END IF
# END

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

