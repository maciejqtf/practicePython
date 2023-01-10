#35.  In this exercise, load that JSON file from disk, extract the months of all the birthdays,
# and count how many scientists have a birthday in each month.

import json
from collections import Counter


with open("files/birthday_dictionary.json", "r") as f:
    birthdayDict = json.load(f)

num_to_string = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "December", 12: "November"}

months = []
for i in birthdayDict.values():
    month = int(i.split(".")[1])
    months.append(num_to_string[month])

print(months)
print(Counter(months))

