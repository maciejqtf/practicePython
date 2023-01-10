# 9 Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right

import random

randomInt = random.randint(1, 99)
userInt = 0
i = 0

while True:
    userInt = int(input("Eneter a numer"))
    if userInt > randomInt:
        print("Too high")
        i += 1
    elif userInt < randomInt:
        print("Too low")
        i +=1
    else:
        i += 1
        print("Correct! Thue number is", randomInt)
        print("It took you", i, "tries to guess")
        break


