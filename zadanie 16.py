#16 Write a password generator in Python. Be creative with how you generate passwords
# - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.

"""
TABLICA ASCII :
33 - 47 - znaki specjalne
48 - 57 - cyfry
58 - 64 - znaki
65 - 90 - DUŻE LITERY
91 - 96 - znaki
97 - 122 - małe litery
 - 127 - znaki
"""

import random

def password_generator():

    characters = range(33, 127)
    password = ""
    passwordLenght = int(input("Enter how many characters do you want in your password?"))
    for i in range(passwordLenght):
        password += chr(random.choice(characters))

    return password

print(password_generator())


# czyjeś rozwiązanie :

def randomletters(x,y):
    return chr(random.randint(ord(x), ord(y)))


# Password Generator
def password_generator2():
    capletters = list() # Capital Letters
    smletters = list() # Small Letters
    numbers = list() # Numbers
    symbols = ["!", "@", "#", "$", "%", "*"] # Symbols
    for cap in range(5): # Capital Letters
        capletters.append(randomletters("A","Z"))
    for sm in range(5): # Small Letters
        smletters.append(randomletters("a","z"))
    for num in range(5): # Numbers
        numbers.append(str(random.randint(0,9)))
    password_list = capletters + smletters + numbers + symbols
    random.shuffle(password_list)
    finalpassword = "".join(password_list)
    return finalpassword

print(password_generator2())