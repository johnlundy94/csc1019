# As the user to input a positive integer, n
# Uses a for loop to print all numbers from 1 to n
# Uses a while loop to calculate and print the sum of numbers from 1 to n

# Ex:
    # Enter a positive integer: 5
    # Numbers from 1 to 5:
    # 1
    # 2
    # 3
    # 4
    # 5
    # The sum of numbers from 1 to 5 is 15

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