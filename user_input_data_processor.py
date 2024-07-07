# Input Length Validator Write a script that asks for and checks the length of the user's first name and
# last name. Both should be at least 2 characters long. If not, print an error message.

first_name = input("What is your first?: ")
last_name = input("What is last first?: ")

if 2 > len(first_name):
    print("Your first name should be at least 2 letters long.")
if 2 > len(last_name):
    print("Your last name should be at least 2 letters long.")
else:
    print("Thank you " + first_name.capitalize() + " " + last_name.capitalize() + "!")