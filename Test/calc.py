from array import *
arr = array('i',[])
n= int(input('How many do you want'))
for i in range(n):
    x = int(input('Put the next value in'))
    arr.append(x)

def update():
    x=int(input('Which number do you wanna change?'))
    if x >= n:
        print('That number is not on the list...')
    else:
        arr[x] = int(input('To what number????'))
        print(arr)
print(arr)
update()
