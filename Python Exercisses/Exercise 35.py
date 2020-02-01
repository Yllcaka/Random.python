from collections import Counter
import json
info = {}
with open("JSON.json","r") as f:
    info = json.load(f)
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
maps = []
for x,d in info.items():
    map = int(d.split('.')[1])
    maps.append(Month[map])
c = Counter(maps)
print(c["May"])