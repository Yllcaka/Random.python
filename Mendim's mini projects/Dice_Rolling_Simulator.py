import random


def dice_roll():
    a = random.randint(1, 6)
    print('Rolling the dice,what could it be?')
    print('The way the dice rolled and fell,its showing This number ...', a)

ask = input("Do you wanna roll the dice???")
if ask == 'yes' or ask == 'y':
    dice_roll()
    a = input('do you wanna roll again?')
    while a == 'yes' or a == 'y':
        dice_roll()
        b = input('do you wanna roll again?')

        if b == 'yes' or b == 'y':
            continue
        elif b == 'no' or b == 'n':
            print('Alright, have a nice day')
            break
        else:
            print('Not a valid answer')
            break

    else:
        print('Alright, have a nice day')

elif ask == 'no' or ask == 'n':
    askagain = input('Are you sure???')
    if askagain == 'yes' or askagain == 'y':
        print("Ok, I guess I'm gonna exterminate my entire existence, You cruel MONSTER...")
    elif askagain == 'no' or askagain == 'n':
        ask_once_again = input('You wanna try again than?')
        if ask_once_again == 'yes' or ask_once_again == 'y':
            dice_roll()
        elif ask_once_again == 'no' or ask_once_again == 'n':
            print("Guess I'll die!")
        else:
            print("That isn't a valid answer,at the least not one I can understand")
    else:
        print("That isn't a valid answer,at the least not one I can understand")
        print("It isn't really worth trying anymore with somebody like you, bye")
else:
    print('Be clear and try again from the beginning')
