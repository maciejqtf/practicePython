#5 write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for item in a:
    if item in b:
        c.append(item)


print("c:",c)

import random

a = []
b = []
for x in range(0,11):
    a.append(random.randint(0, 20))
    b.append(random.randint(3, 24))
a.sort()
b.sort()

print(a, '\n',b, '\n')
print(list(dict.fromkeys([i for i in a if i in b])))