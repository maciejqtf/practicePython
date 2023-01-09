# 14. Write a program (function!) that takes a list and returns a new list that contains
# all the elements of the first list minus all the duplicates.

# USING LOOP :

myList = [1,1,1,2,3,2,3,4,5,66,54,345,43,54,54,54,23,24,17,95,65,65,54,48,13,12,2,1,2]
myList2 = [1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
myList3 = [1,1,1,1,"cat","cat", "Cat", "dog","dog"]


def list_without_duplicates(list):
    newList = []
    for i in list:
        if i not in newList:
            newList.append(i)
    return newList


print(list_without_duplicates(myList))
print(list_without_duplicates(myList2))
print(list_without_duplicates(myList3))

# USING SETS :


def list_without_dups(userList):
    newList = list(set(userList))
    return newList

print(list_without_dups(myList))
print(list_without_dups(myList2))
print(list_without_dups(myList3))

