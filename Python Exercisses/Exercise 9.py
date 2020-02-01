import random
a = random.randint(1,10)
b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
while quit !='Quit' :
    if b==a:
        print("That's it the number I thought about is ",a)
        ask = input('You wanna play again')
        if ask == 'yes':
            print('OK let it continue than')
            a = random.randint(1, 10)
            b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
        elif ask == 'no':
            print('alright')
            quit = "Quit"
    elif b > 10:
        print('That number is higher than 10, I said between 1 AND 10')
        b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
    elif b<1:
        print('That number is lower than 10, I said between 1 AND 10')
        b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
    elif b<a:
        print('That number is too low')
        b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
    elif b>a:
        print('That number is too high')
        b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))
    else:
        print('Please enter a number')
        b = int(input("I'm thinking of a number between 1 and 10 try to guess what number it is"))