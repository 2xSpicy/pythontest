# For Looping

num = [1,2,3,4,5,6,7]

for i in num:
    print('hi')

name = ['Noe','Kyi','Myat','Noe','Htet']

for x in name:
    print(f'hello {x}!')

# range >> Generator

for u in range(0,5):
    print('Hello')


#  While loop >> work with condition

# year = int(input("Insert your birth year: "))
year = 2004
age = 0
while year <= 2024:
    print(f'You are {age} in {year}')
    age += 1
    year += 1

# Normal 
oldlst = [1,2,3,4,5]
newlst = []

for x in oldlst:
    newlst.append(x)
    print(newlst)

# List Comprehension

firstlst = [2,3,4,5,6]
secondlst = [i-1 for i in firstlst]
print(secondlst)

# List Comprehension

even_lst = [i for i in range(1,21) if i%2 == 0]
print(even_lst)

for i in range(1,21):
    if i % 2 == 0:
        even_lst.append(i)
print(even_lst)


# Dictionary comprehension
import random
student = {'mgmg':120,'mya':100,'hla':150,'myat':180}

student_mark = {name:mark -20 for (name,mark) in student.items() if mark==100}
print(student_mark)


stu_name = ['kyi','myat','noe','thant']

stu_w_marks = {name:random.randint(1,100) for name in stu_name}
print(stu_w_marks)