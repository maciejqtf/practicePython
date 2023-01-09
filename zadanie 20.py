#20 Write a function that takes an ordered list of numbers
# (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints)
# an appropriate boolean.
link = "https://www.practicepython.org/exercise/2014/11/11/20-element-search.html"

listA = [1,2,4,5,32,43,2,1,56,76,87,65,45,44,32,35,38,75,5,7,8,3,0,0,6,34,12,34,32,67,86,54,32]
listA.sort()


def number_in_list(list,number):
    if number in list:
        return True
    else:
        return False


if __name__ == "__main__":
    print(number_in_list(listA,1))
    print(number_in_list(listA,199))
    print(number_in_list(listA,2))
    print(number_in_list(listA,12345345))

