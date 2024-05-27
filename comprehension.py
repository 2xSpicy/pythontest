import random

# list comprehension

mark = [1,2,2,3,4,4342,52344,23421,21,43,584,213,2,5,2,3,32,23,45,654]

sorting_mark = [i for i in mark if i>100]
print(sorting_mark)



# Dictionary comprehension

ppl = {'su':26,'thant':20,'t':25}

ppl_nextyear ={ name:age+1 for (name,age) in ppl.items()}
print(ppl_nextyear)


human = ['kaung','lynn','thant','su','myat','noe']

stuWm = {luu:random.randint(0,100) for luu in human}
print(stuWm)


# List comprehension test2

gf = ['su','myat','noe']

gfname = [i for i in gf]
print(gfname)

nn = { name:random.randint(1,100) for name in gf }
print(nn)

# Dictionary Comprehension test2

nickn = {'su': 99, 'myat': 1, 'noe': 55}
nn_update = { name:namecode+1 for (name,namecode) in nickn.items() }


def add():
    a = int(input('enter number: '))
    b = int(input('enter number: '))

    return print(a+b)


print(add())