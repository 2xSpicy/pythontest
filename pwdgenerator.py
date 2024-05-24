import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = [1,2,3,4,5,6,7,8,9]
schars = ['!','@','#','$','%','^','&','*','?']

letter_lst = []
num_letter = int(input('Enter number of letter: '))
num_num = int(input('Enter number of num: '))
num_schar = int(input('Enter number of schar: '))


for x in range(0,num_letter):
    index = letters[random.randint(0,len(letters)-1)]
    letter_lst.append(index)
    
for x in range(0, num_num):
    index = nums[random.randint(0, len(nums)-1)]
    letter_lst.append(index)

for x in range(0, num_schar):
    index = schars[random.randint(0, len(schars)-1)]
    letter_lst.append(index)

pwd = ''
for x in range(0, len(letter_lst)):
    shuffle = letter_lst[random.randint(0, len(letter_lst)-1)]
    pwd = pwd + str(shuffle)
    
print(pwd)