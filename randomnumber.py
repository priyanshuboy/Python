
import random

x = random.randint(1,100)
print(x)

mylist = [
    'hello' ,
    'world',
    'python',
]

y = random.choice(mylist)
print(y)

card = ['1','2','3','4','5','6','7','8','9' ,'a','b','c','d','e','f']

random.shuffle(card)
print(card)