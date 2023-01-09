#lista randomowych numerow
import random

myList = []
for i in range(10):
    myList.append(random.randint(35,135))

print(myList)

newList = [random.randint(1,9) for i in range(10)]
print(newList)