a = int(input('Enter a number '))
if a % 2 == 0:
    print('The number is a even number')
    if a % 4 == 0:
        print('The number is quad')
else:
    print('The number is odd')
num = int(input('Enter another number'))
check = int(input('Enter a divisor'))
if num % check == 0:
    print('The divide evenly')
else:
    print('Why you putting this input')