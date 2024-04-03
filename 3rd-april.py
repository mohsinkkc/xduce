import logging
'''
arguments and keyword arguments
'''
def funct(*args,**kwargs):
    print("The arguments are",args)
    print("the keyword arguments is :",kwargs)

funct(1,2,3,5,8,name='mohsin',age=30,address='narol')


def my_fun(**kwargs):

    print("the kew word arguments are:")
    for key,values in kwargs.items():
        print(f"{key}:{values}")

my_fun(name="mohsin",age=40,height=5.5,address='CG road')
#============================================================================================================================
'''
decoator function
'''
def dec(fun):
    def wraper():
        print("hello decorator ")
        fun()
        fun()
        print("hello decorator ")
    return wraper
@dec
def my_fun():
    print("hello")
my_fun()
#=====================================================

def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function with arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function
def add(x, y):
    return x + y

@log_function
def name(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")

name(name='mohsin',age=41)
result = add(3, 5)

print("Result:", result)

#=========================lamda ================================

add = lambda x,y:x+y
print("the result is :",add(3,4))

