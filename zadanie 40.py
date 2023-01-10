# 40

import random
import sys

randomInt = random.randint(1, 9)
userInt = 0
counter = 0

while True:
    try:
        userInt = int(input("Eneter a numer"))
        if userInt > 9:
            print("Numer is out of range!")
        elif userInt > randomInt:
            print("Too high")
            counter += 1
        elif userInt < randomInt:
            print("Too low")
            counter +=1
        else:
            counter += 1
            print("Correct! Thue number is", randomInt)
            print("It took you", counter, "tries to guess")
            break
    except ValueError:
        print("Something went wrong!", sys.exc_info()[0], "please try again")

