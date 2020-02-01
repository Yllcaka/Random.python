import random
def orderednumber():
    list = []
    x = random.randint(1,9)
    for i in range(7):
        list.append(x)
        x = x + random.randint(1,9)
    return list
a = int(input('enter a number '))
if a in orderednumber():
    print('yes it is in the list')
else:
    print('no it is not in the list')