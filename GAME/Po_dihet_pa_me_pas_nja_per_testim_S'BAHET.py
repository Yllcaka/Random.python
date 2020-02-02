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
lista = [1,2,3,4,5,6,7,8,9]

for i in lista:
    if i == 3:
        i = 10
print(lista)