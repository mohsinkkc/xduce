#class
# single Inheritance

# class Student:
#     def __init__(self,name,age):
#         print("Enter the Details of students")
#         self.name=name
#         self.age=age

# s1=Student("mohsin",29)
# print(f"name is :{s1.name} and age : {s1.age}")

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