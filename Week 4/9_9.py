try:
#   here we are trying to convert the input to an integer and handle possible errors
  speed = int(input("Enter speed: "))
  print("The speed plus 5 is:", speed + 5)
except ValueError:
  speed = int(input("Enter a valid number: "))
  print("The speed plus 5 is:", speed + 5)
input("Enter to exit")

