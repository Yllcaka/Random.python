def binary(list,number):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low+high)//2
        print(mid)
        if list[mid] == number:
            print(f"Tis the place where the number is lallalalalalalalala {mid}")
            break
        elif list[mid] < number:
            low = mid + 1
        elif list[mid] > number:
            high = mid-1
    print("The number is nowhere to be found on the list")

list = []
for i in range(1000):
    if i % 2 != 0:
        list.append(i)
binary(list,16)