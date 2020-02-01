from array import *
arr =array('i',[])
n=int(input('How many do you want?'))
for i in range(n):
    x=int(input('Enter the values'))
    print(i)
    print(x)
    arr.append(x)
print(arr)

val=int(input('Which one do you wanna pick?'))

k=0

for e in arr:
    if e==val:
        print(val,"is  number",k+1)
        break
    k+=1
else:
    print('That number is not in the list')