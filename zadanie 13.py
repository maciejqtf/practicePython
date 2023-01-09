# 13 Write a program that asks the user how many Fibonacci numbers to generate and then generates them. Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.


def fibonacci_generator():
    userInput = int(input("Enter how many number you want to generate"))
    i = 1
    if userInput == 0:
        return []
    elif userInput == 1:
        return [1]
    elif userInput == 2:
        return [1,1]
    elif userInput > 2:
        fib = [1,1]
        while i < (userInput - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
        return fib


print(fibonacci_generator())


"""num=int(input("Enter for how many numbers you want the fibonnaci series: "))
b=[1,1]
for i in range(1,num-1):
    b.append(b[i]+b[i-1])
print(b)"""

