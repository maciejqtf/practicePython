#36 In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!

from bokeh.plotting import figure, show, output_file
import json

output_file("plot.html")

with open("files/birthday_dictionary.json", "r") as f:
    birthdayDict = json.load(f)

x_categories = [i for i in birthdayDict.keys()]
y_categories = [i for i in birthdayDict.values()]
print(x_categories)
x = [i for i in birthdayDict.keys()]
y = [i for i in birthdayDict.values()]


p = figure(x_range=x_categories, y_range=y_categories)

p.vbar(x=x , top=y, width=0.5)

show(p)