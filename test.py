import random

letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


num_letter = int(input('Enter number of letter: '))


for num_letter in range(1,len(letter)):
    
    random_sys = random.randint(1,len(letter))
    print(random_sys)
    letter_lst = [letter.pop(random_sys)]
    

    num_letter -= 1