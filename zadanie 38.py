# 38 Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old),
# except use f-strings instead of the + operator to print the resulting output message.

import datetime

name = input("What's your name ?")
age = int(input("Hoe old are you ?"))
currentYear = datetime.date.today().year
year100 = currentYear - age + 100

print(f"Hey {name}, you will turn 100 in {year100}")
