a = int(input('Enter a number'))
x = range(1,a)
b=[]
for i in x:
    if a%i == 0:
        b.append(i)
print(b)