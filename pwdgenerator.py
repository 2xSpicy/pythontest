import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = [1,2,3,4,5,6,7,8,9]
schars = ['!','@','#','$','%','^','&','*','?']

letter_lst = []
num_lst = []
schar_lst = []

num_letter = int(input('Enter number of letter: '))
num_num = int(input('Enter number of num: '))
num_schar = int(input('Enter number of schar: '))

for x in range(0,num_letter):
    index = letters[random.randint(0,len(letters)-1)]
    letter_lst.append(index)
    print(letter_lst)

pwd1 = ''
for y in letter_lst:
    pwd1 += str(y)
    print(pwd1)

for x in range(0,num_num):
    index = nums[random.randint(0,len(nums)-1)]
    num_lst.append(index)
    print(num_lst)

pwd2 = ''
for y in num_lst:
    pwd2 += str(y)
    print(pwd2)

for x in range(0,num_schar):
    index = schars[random.randint(0,len(schars)-1)]
    schar_lst.append(index)
    print(schar_lst)

pwd3 = ''
for y in schar_lst:
    pwd3 += str(y)
    print(pwd3)

fpwd = pwd1 + pwd2 + pwd3
print(fpwd)

pwdlst = list(fpwd)
random.shuffle(pwdlst)
print(pwdlst)

ffpwd = ''
for x in pwdlst:
    ffpwd += x
    
print(ffpwd)