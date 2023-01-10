#33 For this exercise, we will keep track of when our friend’s birthdays are,
# and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays.
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.

import datetime
import json

#maciejWojtyczka= datetime.datetime(1991,8,23).date()

birthdayDict = {"Maciej Wojtyczka" : "1991.08.23", "Janusz Kruk" : "1963.07.12", "Tomasz Kowalski" : "1985.01.02"}

def birthday_dictionary():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in birthdayDict:
        print(i)
    checkDate = input("Who's birthday do you want to look up?")
    for i in birthdayDict:
        if checkDate == i:
            print(i + "'s bithday is", birthdayDict[i])

    # EXTRA : Ask the user for another scientist’s name and birthday to add to the dictionary

    newPerson = input("Add new person to the dictonary:")
    newPersonBirthday = input("Add their birthday date : yyyy.mm.dd")
    newPersonDict = {newPerson : newPersonBirthday}
    birthdayDict.update(newPersonDict)
    print(birthdayDict)

birthday_dictionary()




