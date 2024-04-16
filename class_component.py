#==========================================================class=========================================================================================
# =====================================================single Inheritance==================================================================================

# class Student:
#     def __init__(self,name,age):
#         print("Enter the Details of students")
#         self.name=name
#         self.age=age

# s1=Student("mohsin",29)
# print(f"name is :{s1.name} and age : {s1.age}")



#=================================================Data Encapsulation and Abstraction program=============================================================
class Account:

    def __init__(self,acc,bal):
        self.acc=acc
        self.bal=bal

    def debit(self,amount):
        self.bal -= amount
        print(f"the amount debites from your account is :{amount}")
        print("the total amount is ",self.get_balance())

    def credit(self,amount):
        self.bal += amount
        print("the Amount Credited to your Account is :",amount)
        print("the total amount is ",self.get_balance())


    def get_balance(self):
        return self.bal

ac1=Account("1234",10000)
ac1.debit(500)
ac1.credit(2600)

#=============================================Static method============================================================ 

class Sun:
    @staticmethod
    def hello():
        print("Hello World ")

s1=Sun()
s1.hello()

# To delete the object in class

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

# class Benz(Car):
#     def __init__(self,name):
#         self.name=name

# m1=Benz("M4")
# print(m1.name)
# m1.start()

#=======================================================Multi Level Inheritance======================================================



