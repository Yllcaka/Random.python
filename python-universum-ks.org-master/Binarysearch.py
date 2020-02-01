def binary(list,number):

    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low + high) // 2
        print(mid)
        if list[mid] == number:
            return f"{number} is on index [{mid}] of the list"
        elif list[mid] < number:
            low = mid+1
        elif list[mid] > number:
            high = mid-1
    return f"{number} isn't in the list"

array = [2,4,6,8,10,12,14]
print(binary(array,14))