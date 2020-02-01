a = 5
b = 3

try:
    print('The Beginning')
    print(a/b)
    k = int(input('Put a number'))
    print(k)
except ZeroDivisionError as e:
    print("Cant't divide by zero")
except ValueError as e:
    print('invalid entry')
except exception as e:
    print('I dunno')
finally:
    print('The End')