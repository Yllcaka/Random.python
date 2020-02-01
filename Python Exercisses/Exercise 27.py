game = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
player1 = 'X'
player2 = 'O'
def PLAYER2():
    position = input(('  Player2  Enter row then column, and seperate them by a comma'))
    position = position.split(',')
    a = int(position[0])
    b = int(position[1])
    if a>2 or b>2:
        print("Please enter a valid option")
        PLAYER2()
    elif game[a][b] != 0:
        print('Try again')
        PLAYER2()
    elif game[a][b] == 0:
        game[a][b] = player2
        print(game)

def PLAYER1():
    position = input(('  "X"  Enter row then column, and seperate them by a comma'))
    position = position.split(',')
    a = int(position[0])
    b = int(position[1])
    if a>2 or b>2:
        print("Please enter a valid option")
        PLAYER1()
    elif game[a][b] != 0:
        print('Try again')
        return PLAYER1()
    elif game[a][b] == 0:
        game[a][b] = player1
        print(game)
true = True
while true:
    PLAYER1()
    PLAYER2()
    # for i in game:
    #     if i != 0:
    #         true = False