

stop = False
Start = input('Do you wanna play a game of Rock,Paper,Scissors?')
if Start == 'yes':
    while not stop:
        player1 = input('Rock,Paper or Scissors')
        player2 = input('Rock,Paper or Scissors')
        while player1 == player2:
            print("That's a draw")
            player1 = input('Rock,Paper or Scissors')
            player2 = input('Rock,Paper or Scissors')
        if player1 == 'Rock' and player2 == 'Paper':
            print('Player2 Won')
        elif player1 == 'Rock' and player2 == 'Scissors':
            print('Player1 Won')
        elif player1 == 'Paper' and player2 == 'Rock':
            print('Player1 Won')
        elif player1 == 'Paper' and player2 == 'Scissors':
            print('Player2 Won')
        elif player1 == 'Scissors' and player2 == 'Paper':
            print('Player1 Won')
        elif player1 == 'Scissors' and player2 == 'Rock':
            print('Player2 Won')
        else:
            print("That isn't a valid answer")
            player1 = input('Rock,Paper or Scissors')
            player2 = input('Rock,Paper or Scissors')
        new = input('Do you wanna start a new game?')
        if new =='yes':
            print('starting new game')
        else:
            stop = True
            print('Screw you I guess')
elif Start == 'no':
    print('Goodbye')
else:
        print("That isn't a valid answer")