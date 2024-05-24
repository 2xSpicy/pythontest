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

evenlst = [i for i in range(1,21) if i%2 == 0]
print(evenlst)

even_lst = []
for i in range(1,21):
    if i % 2 == 0:
        even_lst.append(i)
print(even_lst)

    