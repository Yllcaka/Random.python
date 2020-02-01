list = []
for i in range(1,101):
    list.append(i)
print(list)
min = 0
max = len(list)-1
guess = 0
while min <=max:
    mid = (max+min)//2
    b = input('Is this the right number ,or is it higher or lower '+ str(mid)+' ')
    if b.startswith('y'):
        if guess>5:
            print('Alright so the number is',mid,'an it took only ',guess,' guesses...yep only ',guess,'guesses... \n*cries in binary')
        else:
            print('Alright so the number is',mid,'an it took only ',guess)
        break
    elif b.startswith('h'):
        min = mid+1
        guess+=1
    elif b.startswith('l'):
        max = mid-1
        guess+=1
    else:
        print('Please enter something valid  ')