# 34.  modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
# rather than having the dictionary defined in the program.

import json


def birthday_dictionary():
    with open("files/birthday_dictionary.json", "r") as file:
        birthdayDict = json.load(file)
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in birthdayDict:
        print(i)
    checkDate = input("Who's birthday do you want to look up?")
    for i in birthdayDict:
        if checkDate == i:
            print(i + "'s bithday is", birthdayDict[i])

    # Asking for the new person
    newPerson = input("Add new person to the dictonary:")
    newPersonBirthday = input("Add their birthday date : yyyy.mm.dd")
    birthdayDict[newPerson] = newPersonBirthday

    with open("files/birthday_dictionary.json", "w") as file:
        json.dump(birthdayDict, file)
    print(birthdayDict)


birthday_dictionary()