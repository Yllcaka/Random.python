player1 = 'X'
player2 = 'O'


def Board():
    c = 0
    for i in range(3):
        print('  -----  ' * 3)
        print(f' |  {game[i][0]}  |  |  {game[i][1]}  |  |  {game[i][2]}  | ')
        c += 1
    print('  -----  ' * 3)


game = [
    [' ' , ' ' , ' '] ,
    [' ' , ' ' , ' '] ,
    [' ' , ' ' , ' ']
]


def PLAYER2(game):
    position = input(('  "O"  Enter row then column, and seperate them by a comma'))
    position = position.split(',')
    a = int(position[0])
    b = int(position[1])
    if a > 2 or b > 2:
        print("Please enter a valid option")
        PLAYER2(game)
    elif game[a][b] != ' ':
        print('Try again')
        PLAYER2(game)
    elif game[a][b] == ' ':
        game[a][b] = player2
        Board()
    CHECK(game)


def PLAYER1(game):
    position = input(('  "X"  Enter row then column, and seperate them by a comma'))
    position = position.split(',')
    a = int(position[0])
    b = int(position[1])
    if a > 2 or b > 2:
        print("Please enter a valid option")
        PLAYER1(game)
    elif game[a][b] != ' ':
        print('Try again')
        return PLAYER1(game)
    elif game[a][b] == ' ':
        game[a][b] = player1
        Board()
    CHECK(game)


def CHECK(makarena):
    for x in range(3):
        if makarena[x][0] == makarena[x][1] and makarena[x][1] == makarena[x][2] and makarena[x][0] != ' ':
            print(makarena[x][0] + ' WON')
            return False

    for x in range(3):
        if makarena[0][x] == makarena[1][x] and makarena[1][x] == makarena[2][x] and makarena[0][x] != ' ':
            print(makarena[0][x] + ' WON')
            return False

    if makarena[0][0] == makarena[1][1] and makarena[1][1] == makarena[2][2] and makarena[0][0] != ' ':
        print(makarena[1][1] + ' WON')
        return False
    if makarena[2][0] == makarena[1][1] and makarena[1][1] == makarena[0][2] and makarena[2][0] != ' ':
        print(makarena[1][1] + ' WON')
        return False

def moves_exist(game):
	for row_num in range(3):
		for col_num in range(3):
			if game[row_num][col_num] == ' ':
				return True
	return False
Board()
while True and moves_exist(game):
    if CHECK(game) == False:
        break
    PLAYER1(game)
    PLAYER2(game)
