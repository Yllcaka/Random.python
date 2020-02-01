import random
a = random.randint(1,100)
print('I just thought of a number between 1 and 100')
b = int(input('Guess what it is...'))
while b != a:
    if b == None:
        b= int(input("Please enter a number"))
    elif b>100:
        b = int(input("You're kidding me right?..."))
    elif b<1:
        b = int(input("Only a jedi would go that low,\nTry again..."))
    elif b < a-20:
        print("That's far too low...")
        b = int(input('Guess again...'))
    elif b > a+20:
        print("That's far too high...")
        b = int(input('Guess again...'))
    elif b < a-10:
        b = int(input("That's too low..."))
    elif b > a+10:
        b = int(input("That's too high..."))
    elif b > a:
        b = int(input('Lower...'))
    elif b < a:
        b = int(input('Higher...'))
print("That's right the number is " ,a)