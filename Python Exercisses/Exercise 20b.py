pos = -1


def binarysearch(list, a):
    min = 0
    max = len(list) - 1
    while min <= max:
        mid = (max + min) // 2
        if list[mid] == a:
            globals()['pos'] = mid
            return True
        elif list[mid] < a:
            min = mid+1
        else:
            max = mid - 1
    return False


list = [1, 2, 4, 6, 8, 11]
a = int(input('Enter a number   '))
if binarysearch(list, a):
    print('YATA!!!')
else:
    print('Awwwww maaaaan')
