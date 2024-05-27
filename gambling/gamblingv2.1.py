# p1_balance = int(input('Enter deposit amount: '))
# p2_balance = int(input('Enter deposit amount: '))
# p3_balance = int(input('Enter deposit amount: '))
# p4_balance = int(input('Enter deposit amount: '))

p1_balance = 0
p2_balance = 1000
p3_balance = 1000
p4_balance = 1000

game_on = True
winner = int

def balance():
    print(f'Player1\'s balance: {p1_balance}')
    print(f'Player2\'s balance: {p2_balance}')
    print(f'Player3\'s balance: {p3_balance}')
    print(f'Player4\'s balance: {p4_balance}')

while game_on:
    winner == int(input('Winner: '))

    if p1_balance == 0 or p2_balance == 0 or p3_balance == 0 or p4_balance == 0:
        print('Low Balance!!')
        balance()

        print('Deposit: 1\n End a game: 2')
        usr_choice = int(input('Enter your choice: '))

        if usr_choice == 1:
            deposit = True

            # deposit instruction
            print('Deposit into player1\'s Balance: 1 \nDeposit into player1\'s Balance: 2 \nDeposit into player1\'s Balance: 3 \nDeposit into player1\'s Balance: 4 \nCheck Balance: 5 \nEnd deposit: 6')

            while deposit:
                if usr_choice == 1:
                    amount = int(input('Deposit amount: '))
                    p1_balance += amount
                    print(f'Your amount: {p1_balance}')
                
                elif usr_choice == 2:
                    amount = int(input('Deposit amount: '))
                    p2_balance += amount
                    print(f'Your amount: {p2_balance}')

                elif usr_choice == 3:
                    amount = int(input('Deposit amount: '))
                    p3_balance += amount
                    print(f'Your amount: {p3_balance}')

                elif usr_choice == 4:
                    amount = int(input('Deposit amount: '))
                    p4_balance += amount
                    print(f'Your amount: {p4_balance}')

                elif usr_choice == 5:
                    balance()

                elif usr_choice == 6:
                    deposit = False

                else:
                    print('Check Your Number!!')


        print('\n')

    if winner == 1:
        p1_balance += 300
        p2_balance -= 100
        p3_balance -= 100
        p4_balance -= 100
        
        balance()
        print('\n')

    elif winner == 2:
        p1_balance -= 100
        p2_balance += 300
        p3_balance -= 100
        p4_balance -= 100
        
        balance()
        print('\n')

    elif winner == 3:
        p1_balance -= 100
        p2_balance -= 100
        p3_balance += 300
        p4_balance -= 100
        
        balance()
        print('\n')

    elif winner == 4:
        p1_balance -= 100
        p2_balance -= 100
        p3_balance -= 100
        p4_balance += 300
        
        balance()
        print('\n')
    
