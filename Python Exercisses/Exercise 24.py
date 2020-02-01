def Board(a,b):
        for i in range(a):
            print(' --- '*b)
            print('|   |'*b)
        print(' --- '*b)
a = int(input('How many rows'))
b = int(input('How many columns'))
Board(a,b)