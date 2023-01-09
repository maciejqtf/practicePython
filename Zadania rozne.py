
# https://www.practicepython.org/

#1. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

name = input("What's your name ?")
age = int(input("How old are you?"))
year = datetime.date.today().year
print("Hey", name, "You will turn 100 in", str(year - age + 100 ))


#2. Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


num = int(input("Please type a number"))
check = int(input("Please type a possible divider"))
if num % 4 == 0:
    print("The number is even and divisible by 4")
elif num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

if num % check == 0:
    print(num, "is dividable by", check)
else:
    print(num, "is not dividable by", check)




