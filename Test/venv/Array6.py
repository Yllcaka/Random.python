def update():
    x = int(input('Which number do you wanna change?'))
    if x > 2:
        print('There arent as many numbers in this list')
    else:
        spam[x] = int(input('To what number'))
        print(spam)


spam = [1, 2, 3]
print(spam)
update()
