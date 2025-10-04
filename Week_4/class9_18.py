# conditional executions
# This is considered a compound statement 

x = 5

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is 0")
else:
    print("x is negative")

#  Nested conditionals


if x < 0:
    print("x is negative")
    if x > 0:
        print("x is positive")

weight = int(input("Weight in kilos:"))
print(f"Your weight is", weight)

# syntax of split(specific char, max split)
data = "apple, banana, cherry"
print(data.split(" ", 1))



