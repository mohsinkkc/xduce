'''from dataclasses import dataclass

@dataclass
class Info:
    name:str
    gender:str
    phone_number:int
    address:str 

l1=Info("mohsin","male",7898986561,"CG road")
l2=Info("dehanshu","male",9898154688,"Kalupur")

print(l1)
print(l2)
'''
#===========================Prime ======================================
'''
def prime(a):
    if a==1:
        print("the number is not prime")
    elif a>1:
        for i in range(2,a):
            if a%i:
                print("the number is prime")
                break
            else:
                print("the number is not prime")
                break

a=int(input("enter the nmber:"))
print(prime(a))
'''
#==============================palidrome ======================================
'''def pali(b):
    temp=0
    reverse=0
    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp //= reverse
        if reverse == b:
            print("the number is palidrome")
        else:
            print("the number is not palidrome")
b=input("enter the number :")
print(pali(b))
'''
#=============================Decorator ==========================
''' def decore(func):
    def wrapper():
        func()
        print("hello , Good Morning ")
       
    return wrapper
@decore
def my():
    print("Have Nice Day")

my()
'''
#==================Args & Kwargs====================
'''def argumnets(*args,**kwargs):
    print("the Argumnets are",args)
    print("The Keyword Arguments are :",kwargs)

argumnets(1,1,5,4,9,name="mohsin",age=26)
'''
#========================Dictionary Comphernsive=================
'''d1={"apple":"red","banana":"yellow","grapes":"green","watermelon":"red","kiwi":"green"}
#d2={key:values for key,values in d1.items()}
d2={key: ("green" if values == "green" else "red" ) for (key,values) in d1.items()}



print(d2)
'''

