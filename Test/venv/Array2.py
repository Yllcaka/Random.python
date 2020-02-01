from array import *

arr=array('i',[])
n=int(input('Enter how many you want'))
for i in range(n):
    x=int(input('put in the next value'))
    arr.append(x)
print(arr)
val= int(input('Which one do you wanna search?'))
k=0
for e in arr:
    if e == val:
        print("It's on row" ,k+1)
        break
    k+=1
else:
    print("This number isn't in the path of existence")
