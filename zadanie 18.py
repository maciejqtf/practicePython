#18 Create a program that will play the “cows and bulls” game with the user.
exercise = "https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html"

import random

def cows_and_bulls():
    randomNumber = str(random.randint(1000,9999))
    print("Welcome to the Cows and Bulls game!")

    while True:
        cows = 0
        bulls = 0
        i = 0
        userGuess = input("Enter a 4 digit number")
        
