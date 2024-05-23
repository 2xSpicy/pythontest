
import random

r = """
        ________
    ---'    ____)
           (______)
           (______)
           (_____)
    ---.___(____)
    """

p = """
        ________
    ---'     ____)_____
                _______)
                ________)
              ________)
    ---.___________)
    """

s = """
         _______
    ---'   ____)_____
              _______)
           ___________)
           (____)
    ---.__(___)
    """


game = [r,p,s]

sys_rd = random.randint(0,2)
sys_randon = game[sys_rd]
# print(sys_randon)

print(f'Rock : Enter\"0\" \n\t{r}')
print(f'Paper : Enter\"1\" \n\t{p}')
print(f'Scissor : Enter\"2\" \n\t{s}')

usr_c = int(input("Enter your choice: "))
user_pick = game[usr_c]

print(f'\nPlayer\'s choice {usr_c} \n{user_pick}')
print(f'\nSystem\'s choice {sys_rd} \n{sys_randon} ')

if user_pick == sys_randon:
    print('Draw')

elif usr_c == 0 and sys_rd == 1:
    print('You Lose!!')

elif usr_c == 0 and sys_rd == 2:
    print('You Win!!')

elif usr_c == 1 and sys_rd == 0:
    print('You Win!!')

elif usr_c == 1 and sys_rd == 2:
    print('You lose!!')

elif usr_c == 2 and sys_rd == 0:
    print('You Lose!!')

else:
    print('You Win!!')