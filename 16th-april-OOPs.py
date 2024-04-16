#==========================================================class=========================================================================================
# ======================================================================================================================================================

class Student:
    def __init__(self,name,age):
        print("Enter the Details of students")
        self.name=name
        self.age=age

s1=Student("mohsin",29)
print(f"name is :{s1.name} and age : {s1.age}")

#===========================================Calculator task======================================================================================
class Cal:
    def add(self):
        self.n1=int(input("enter the number 1:"))
        self.n2=int(input("enter the number 2:"))
        return self.n1+self.n2
    def sub(self):
        return self.n1-self.n2
    def mul(self):
        return self.n1*self.n2

ob1=Cal()
print("the addition is :",ob1.add())
print("the sub is :",ob1.sub())
print("the multiplication is :",ob1.mul())

#=================================================Customer Account details task =============================================================
class Account:
    def __init__(self,acc_no,balance):
        
        
        self.acc_no=acc_no
        self.balance=balance

    def debit(self,debit_amount):
        self.balance -= debit_amount
        print(f"the amount if Rs {debit_amount} is debited from your account, the account number is : {self.acc_no} and the balance available is :",self.get_balance())

    def credit(self,credit_amount):
        self.balance += credit_amount
        print(f"the amount of Rs {credit_amount} is credited to your account , the account number is :{self.acc_no} and the balance available is :",self.get_balance())

    def get_balance(self):
        return self.balance


acc_no=int(input("Enter the account number :"))
balance=0
c5=Account(acc_no,balance)
credit_amount=int(input("enter the amount to Credited :"))
debit_amount=int(input("enter the amount to be Debit:"))
c5.credit(credit_amount)
c5.debit(debit_amount)
print(f"from the Account : {c5.acc_no} the Available Balance in your account is : {c5.get_balance()}")

#=============================================Static method============================================================ 

class Sun:
    @staticmethod
    def hello():
        print("Hello World ")

s1=Sun()
s1.hello()

# ================================================To delete the object in class============================================================

class Teacher:
    def __init__(self,name):
        self.name=name

n1=Teacher("Mohsin")
print(n1.name)
# del n1
# print(n1)

#===================================================== Private Class========================================================================= 
''' To Acccess the private funtion we cannot access it from outside the class only the inside person can access the private name or anything that was in private
'''
class Person:
    def __Hi(self):
        print("hello Everyone")

    def World(self):
        self.__Hi()

h1=Person()
h1.World()

#============================================================= Inheritance =====================================================================================

#============================================================= Single Inheritance ==============================================================================

class Car:
    @staticmethod
    def start():
        print("the Car has been Started..")
    @staticmethod
    def stop():
        print("the car Has been Stop ...")

class Benz(Car):
    def __init__(self,name):
        self.name=name

m1=Benz("M4")
print(m1.name)
m1.start()

#=======================================================Multi Level Inheritance======================================================
class Car:
    @staticmethod
    def start():
        print("the Car has been Started..")
    @staticmethod
    def stop():
        print("the car Has been Stop ...")

class Toyota(Car):

    def __init__(self,brand):
        self.brand=brand

class Pirus(Toyota):
    def __init__(self,type):
        self.type=type

car1=Pirus("Petrol")
car1.start()


#==================================================== Multiple Inheritance ===========================================
class A:
    var1="welcome to A"

class B:
    var2="welcome to B"

class C(A,B):
    var3="welcome to C"

c1=C()

print(c1.var1)
print(c1.var2)

#=================================================Super()==============================================
'''
To access the method from the Parents class
'''
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("The Car has been Started..")
    @staticmethod
    def stop():
        print("The Car has Stoped")

class Toyota(Car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1=Toyota("Prius","Electric")
print(car1.type)

#====================================================================Class Method =====================================================
'''
There are many ways to access class method 
1) we use @classmethod 
2)self.classname.name="xyz"

'''

class Person:
    name="Moin"

    @classmethod
    def changename(cls,name):
        # self.Person.name="mohsin"
        cls.name=name

p1=Person()
p1.changename("mkkc")
print(p1.name)

#====================================================@property Decorator===================================================
'''
It is the property where after we have make changes outside the class it will automatically change by itself with help of @property decorator

'''

class Student:
    def __init__(self,math,english,gk):
        self.math=math
        self.english=english
        self.gk=gk

    @property
    def percentage(self):
        result = (self.math + self.english + self.gk)/3
        result = str(result)+'%'
        print(result,type(result))
        return result

st1=Student(78,56,95)
print(st1.percentage)
st1.gk=85
print(st1.percentage)

#=====================================================================================================================================================================
class Info:
    def __init__(self,dept,role,salary):
        self.dept=dept
        self.role=role
        self.salary=salary

    def Details(self):
        print("Department =",self.dept)
        print("Role =",self.role)
        print("Salary =",self.salary)

class Engineer(Info):
    def __init__(self,age,name):
        self.name=name
        self.age=age
        super().__init__("Enginerr","It","80000")

d1=Engineer("29","mohsin")
print(d1.Details())

#========================================Area and Perimeter of Circle==========================================================================================
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        return self.radius **2

    def Perimeter(self):
        return 2*3.14*self.radius

jk=Circle(21)
print("the area of circle is :",jk.Area())
print("the perimeter of circle is :",jk.Perimeter())

#===============================================================Dender method========================================================================================
#using __gt__()
class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
    
    def __gt__(self,c2):
        return self.price > c2.price

c1=Order("tea",25)
c2=Order("bun",35)


print(c1 > c2)






