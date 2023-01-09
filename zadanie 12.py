#12 Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.


def list_first_and_last():
    userInput = input("Please enter numbers separated with coma")
    userList = list(userInput.split(","))
    print(userList)
    print(userList[0], userList[-1])


list_first_and_last()