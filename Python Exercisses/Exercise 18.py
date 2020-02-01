import random

num = '0123456789'


def randomcodegenerator(num):
    code = ''.join(random.sample(num, 4))
    return code


def compare(guess, code):
    bullcow = [0, 0]
    a = []
    b = []
    for x, y in zip(guess, code):
        if x == y:
            bullcow[0] += 1
        else:
            a.append(x)
            b.append(y)
    for x in a:
        if x in b:
            bullcow[1] += 1
            a.remove(x)
    return bullcow


def playAgain():
    print('You wanna play again?')
    return input().lower().startswith("y")


if __name__ == "__main__":
    attempt = 10
    code = randomcodegenerator(num)
    DONE = False
    while attempt > 0:
        guess = input('Guess what is the number?   ')
        if len(guess) == 4:
            bullcow = compare(guess, code)
            if guess == code:
                print("Yippy!You guessed it the number is :" + code)
                break
            else:
                print('COW: %d' % bullcow[0])
                print('Bull: %d' % bullcow[1])
                attempt -= 1
                print('%d attempts left' % attempt)
        else:
            print('That ain\'t it chef')
        if attempt == 0:
            print('The number you were loking for was ' + code)
            DONE = True
        if DONE :
            if playAgain():
                print('Cows and Bulls')
                attempt = 10
                code = randomcodegenerator(num)
                DONE = False
            else:
                print('See ya then')