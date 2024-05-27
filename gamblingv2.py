player = int(input('player count: '))

if player == 2:

    player1 = 0 
    player2 = 0

    game_on = True
    while game_on:
        winner = int(input('Winner 1 or 2: '))
        if winner == 1:
            player1+=1
        
        elif winner == 2:
            player2+=1

        elif winner == 3:
            game_on = False

    if player1 > player2:
        player1 -= player2
        print(f'Player1 got {player1}')

    elif player2 > player1:
        player2 -= player1
        print(f'Player2 got {player2}')

elif player == 3:


    player1 = 0 
    player2 = 0
    player3 = 0

    game_on = True
    while game_on:
        winner = int(input('Winner 1 or 2 or 3: '))
        if winner == 1:
            player1+=1
        
        elif winner == 2:
            player2+=1

        elif winner == 3:
            player3+=1

        elif winner == 4:
            game_on = False

    if player1 > player2 and player1 > player3:
        print(f'Player1 got {player1} score.')
        print(f'Player2 got {player2} score.')
        print(f'Player3 got {player3} score.')

    elif player2 > player1 and player2 > player3:
        print(f'Player1 got {player2} score.')
        print(f'Player2 got {player1} score.')
        print(f'Player3 got {player3} score.')
        