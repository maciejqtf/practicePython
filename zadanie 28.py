# Implement a function that takes as input three variables, and returns the largest of the three.
# Do this without using the Python max() function!

def max_number(a=1,b=2,c=3):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(max_number())
print(max_number(3,5,7))
print(max_number(9,3,5))
print(max_number(45,3546,45646))

#with user input :

def max_number():
    userList = input("Please enter 3 integers separated with coma").split(",")
    listOfNumbers = [int(i) for i in userList] # zamiany listy stringów na listę intów
    if listOfNumbers[0] > listOfNumbers[1] and listOfNumbers[0] > listOfNumbers[2]:
        return listOfNumbers[0]
    elif listOfNumbers[1] > listOfNumbers[0] and listOfNumbers[1] > listOfNumbers[2]:
        return listOfNumbers[1]
    else:
        return listOfNumbers[2]


print(max_number())

