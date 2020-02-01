pos = -1

def search(list,n):
    l = 0
    u = len(list)-1

    while l <= u:
        mid = (l+u)//2

        if list[mid] == n:
            globals()['pos'] = mid
            return True
        elif list[mid] < n:
            l = mid + 1
        else:
            u = mid - 1
    return False

list = [1,4,6,13,14,166]
n = 13
if search (list,n):
    print('found at' ,pos+1)
else:
    print('not found')