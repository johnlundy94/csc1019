# Conversion from float to integer
print(3.14, int(3.14))

# Value errors often occurs when you are passing the wrong type
# print(int("23bottles"))
# Value Error
# print(int("23"))
# Prints 23

# Stays float type
print(type(float(123.21)))

# ---------------------------------------
# Varbiables 
# convention for variable names
print_me = print(...)
# Must begin with a letter
# Cannot have iegal characters ($) or specific names (class)

# Prints
print(1,000,000)
print(1,777,555,666)
print(67,12,1978,2876)
print(157)
print("157")
# Errors out, will not print anything after
# Print("Hello World")
# print("Hello World"
print("157")

# -------------------------------------
# you can exit python with
# exit()
# # and
# quit()

# --------------------------------------
# An expression produces a value.
# It can be a part of a statement.
# Examples:
# 2 = 3 produces 5
# len("hello")

# 10 is an expression of x = 10
# Think of an expression as something that can be evaluates to a value

# --------------------------------------
# A statement does something but may not produce a value
# Statements often contain expressions, but not all expressions are statements.
# Expression of the statement.
x=5
# Expression of the statement.
print(x)
if x > 0:
    print("Positive")