import random

p1 = 0
p2 = 0

game_on = True
userguess = int(input('Enter your guess "1" or "2": '))

while game_on:
    p1 += random.randint(1,10)
    print(f'Player1\'s score is {p1}.')
    p2 += random.randint(1,10)
    print(f'Player2\'s score is {p2}.')

    if p1 > 100:
        game_on = False
        print(f'Player1 win the game with {p1} score.')
    elif p2 > 100:
        game_on = False
        print(f'Player2 win the game with {p2} score.')

if userguess == 1 and p1 > 100:
    print('You Win!')

elif userguess == 1  and p1 < 100:
    print('You lose!')

elif userguess == 2  and p1 < 100:
    print('You win!')

elif userguess == 2  and p1 > 100:
    print('You lose!')