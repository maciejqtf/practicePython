#23 Given two .txt files that have lists of numbers in them, find the numbers that are overlapping

primeNumbers = "files/one.txt"
happyNumbers = "files/two.txt"

with open(primeNumbers, "r") as file:
    all_text = file.read()
    primeNumbersList = all_text.split()

with open(happyNumbers, "r") as file:
    all_text = file.read()
    happyNumbersList = all_text.split()

overlapping = []

for i in primeNumbersList:
    if i in happyNumbersList:
        overlapping.append(i)

print(overlapping)
