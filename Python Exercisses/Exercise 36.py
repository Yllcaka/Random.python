from bokeh.plotting import figure, show, output_file
import json
from collections import Counter
info = {}
with open("scientist_birthdays.json","r") as f:
    info = json.load(f).values
Month = {
    1: "January" ,
    2: "February" ,
    3: "March" ,
    4: "April" ,
    5: "May" ,
    6: "June" ,
    7: "July" ,
    8: "August" ,
    9: "September" ,
    10: "October" ,
    11: "November" ,
    12: "December"
}
months = []

for map in info():
    map = (map.split('/'))
    month = int(map[0])
    months.append(Month[month])
months = Counter(months)
x = list(months.keys())
y = list(months.values())
output_file("plot.html")
p = figure(x_range = list(Month.values()))
p.vbar(x=x,top = y,width = 0.5)
show(p)