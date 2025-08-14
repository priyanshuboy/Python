#kwargs : parameter that will pack all arguments into a dictionary useful so that a function
#         can accept a varying  amount of keyword arguments

def func(**kwargs):
    print(kwargs['name'] + " " + kwargs['age'])
    for key,value in kwargs.items():
        print(key + ": " + str(value) ,end=' , ')

func(name='bob', age='20')