#36 In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!

from bokeh.plotting import figure, show, output_file
import json
from collections import Counter

output_file("plot.html")

with open("files/birthday_dictionary.json", "r") as f:
    birthdayDict = json.load(f)

num_to_string = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "December", 12: "November"}

months = []
for i in birthdayDict.values():
    month = int(i.split(".")[1])
    months.append(num_to_string[month])

print(months)
print(Counter(months))

x_categories = [i for i in num_to_string.values()]
x = [i for i in Counter(months).keys()]
y = [i for i in Counter(months).values()]

p = figure(x_range = x_categories)
p.vbar(x=x, top=y, width=0.5)

show(p)





"""output_file("plot.html")

with open("files/birthday_dictionary.json", "r") as f:
    birthdayDict = json.load(f)

x_categories = [i for i in birthdayDict.keys()]
y_categories = [i for i in birthdayDict.values()]
print(x_categories)
x = [i for i in birthdayDict.keys()]
y = [i for i in birthdayDict.values()]


p = figure(x_range=x_categories, y_range=y_categories)

p.vbar(x=x , top=y, width=0.5)

show(p)"""