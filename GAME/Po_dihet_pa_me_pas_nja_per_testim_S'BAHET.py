import re
tripi = re.compile(r"(\d\d)-(\d\d\d-\d\d\d)")
teksti = "Numri jane: 43-551-908 , 44-151-645, 43-545-123"
mo = tripi.findall(teksti)
print(mo)
count = 0
for i in mo:
    for j in i:
        if j == "43":
            count+=1
print(count)