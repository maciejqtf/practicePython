#15. Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.

def reversed_strings():
    userStrings = input("Please enter some sentence")
    reversedStringsList = userStrings.split()[::-1]
    reversedStrings = " ".join(reversedStringsList)
    return reversedStrings


print(reversed_strings())