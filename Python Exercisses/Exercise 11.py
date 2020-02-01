def get_prime(a):
    b = [i for i in range(2, a) if a % i == 0]
    if a < 2:
        print("The number shouldn't be lower than 2")
        a = int(input('Enter a number that is at least 2'))
        get_prime(a)
    elif b == []:
        print(a," is a prime number")
        c = input('You wanna try again?')
        if c == 'yes':
            a = int(input('Enter a number that is at least 2'))
            get_prime(a)
        else:
            print('Goodbye')
    elif b != []:
        print(a," is a composite number")
        c = input('You wanna try again?')
        if c == 'yes':
            a = int(input('Enter a number that is at least 2'))
            get_prime(a)
        else:
            print('Goodbye')
    else:
        print('Please enter a valid number')
        c = input('You wanna try again?')
        if c == 'yes':
            a = int(input('Enter a number that is at least 2'))
            get_prime(a)
        else:
            print('Goodbye')

a = int(input('Enter a number that is at least 2'))
get_prime(a)