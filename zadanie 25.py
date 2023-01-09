# 25  You, the user, will have in your head a number between 0 and 100. The program will guess a number,
# and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number

"""numberRange = range(0, 101)
counter = 0

while True:
    myList = [i for i in numberRange]
    print("My guess is", int(round((myList[0] + myList[-1])/2)),)
    answer = input("Is it correct?/too low?/too high?")
    if answer == "yes":
        print("Congratulations!")
        counter =+ 1
        break
    elif answer == "too low":
        numberRange = range(51,101)
        myList = [i for i in numberRange]
        counter += 1
    elif answer == "too high":
        numberRange = range(0, 50)
        myList = [i for i in numberRange]
        counter += 1"""

minNumber = 0
maxNumber = 100
counter = 0
ans = " "

while ans != "yes":
    guess = round((minNumber+maxNumber)/2)
    print(guess)
    ans = input("Is it correct?")
    counter += 1
    if ans == "too high":
        maxNumber = guess
    elif ans == "too low":
        minNumber = guess
    print("It took my", counter, "tries to guess")
