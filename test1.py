import random

letter = [1,2,3,4,5,6,7,8,9,'!','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letter_lst = []
print(type(letter))

num_of_letter = int(input('Letter >> '))
for i in range(0,num_of_letter):
    index = letter[random.randint(0,len(letter)-1)]
    print(index)
    letter_lst.append(index)

print(letter_lst)

pwd = ''
for x in letter_lst:
    pwd = pwd + str(x)
    
print(pwd)