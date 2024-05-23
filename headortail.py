import random

headntail = 1,2
pick = random.choice(headntail)

print('Choose: \n\t1) \"Head\" \n\t2) \"Tail\" \n!! Enter 1 or 2 !!')

usrpick = int(input('Enter your choice: '))

if usrpick == pick:
    print('U make the right choice :3 ')

elif usrpick != pick:
    print('U made the wrong choice :\"(')