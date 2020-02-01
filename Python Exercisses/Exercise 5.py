import random

a = random.sample(range(1,99),20)
b = random.sample(range(1,99),20)
x=[]
for i in b:
    if i in a:
        x.append(i)
print(x)