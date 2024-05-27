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