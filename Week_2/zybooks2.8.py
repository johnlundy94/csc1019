# A variable first defined in names.py is accessed via names.first.

# names.py file
first = "Larry"
last = "David"

# print_name.py file
import names
print(names.first, names.last)