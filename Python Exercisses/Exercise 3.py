a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = int(input('Enter a number'))
print(list(filter(lambda x:(x<=b),a)))