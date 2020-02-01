pos = -1

def search(list,n):
    i=0
    for i in list:
        if i == n:
            globals() ['pos'] = i
            return True
        i += 1



list = [1,6,2,5,4,3]
n = 3
if search (list,n):
    print('found at' ,pos+1)
else:
    print('not found')