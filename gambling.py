player1 = 0 
player2 = 0

game_on = True
while game_on:
    winner = int(input('Winner 1 or 2: '))
    if winner == 1:
        player1+=1
    
    if winner == 2:
        player2+=1

    if winner == 3:
        game_on = False

if player1 > player2:
    player1 -= player2
    print(f'Player1 got {player1}')

elif player2 > player1:
    player2 -= player1
    print(f'Player2 got {player2}')



