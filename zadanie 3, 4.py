#3.Write a program that prints out all the elements of the list that are less than 5.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in numbers:
    if i < 5:
        print(i)

#
newList = []
for i in numbers:
    if i < 5:
        newList.append(i)

print("List of numbers <5",newList)

num = int(input("Please type a number"))
userList = []

for i in numbers:
    if i < num:
        userList.append(i)

print("User's list is", userList)

#4 Create a program that asks the user for a number and then prints out a list of all the divisors of that number

num = int(input("Please type some number"))
listOfDivisors = []

for element in range(1,num+1):
    if num % element == 0:
        listOfDivisors.append(element)

print(listOfDivisors)

