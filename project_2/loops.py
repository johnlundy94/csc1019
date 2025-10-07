# Algorithm:
# 1. Ask the user to input a positive integer n.
# 2. Use a for loop to print all numbers from 1 to n.
# 3. Use a while loop to calculate the sum of all numbers from 1 to n.
# 4. Display the total sum.

# Pseudocode:
# BEGIN
#     PROMPT user to enter a positive integer n
#     DISPLAY "Numbers from 1 to n:"
#
#     FOR i FROM 1 TO n DO
#         DISPLAY i
#     END FOR
#
#     SET sum_total = 0
#     SET i = 1
#     WHILE i <= n DO
#         sum_total = sum_total + i
#         i = i + 1
#     END WHILE
#
#     DISPLAY "The sum of numbers from 1 to n is", sum_total
# END

# User input
n = int(input("Enter a positive integer: "))

# Print numbers from 1 to n using a for loop
print(f"Numbers from 1 to {n}")
for i in range(1, n + 1):
    print(i)

# Calculating the sum using a while loop
sum_total = 0
i = 1
while i <= n:
    sum_total += i
    i += 1

# Print result
print(f"The sum of numbers from 1 to {n} is {sum_total}")