#11 Ask the user for a number and determine whether the number is prime or not.
#You can (and should!) use your answer to Exercise 4

def get_prime_number():
    number = int(input("Please enter a number"))
    divisors = []

    for i in range(2, number):
        if number % i == 0:
            divisors.append(i)

    if len(divisors) == 0:
        print(number, "is a prime number")
    else:
        print(number, "is not a prime number. \n List of divisors :", divisors)

get_prime_number()
