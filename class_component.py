#class
# single Inheritance

class Student:
    def __init__(self,name,age):
        print("Enter the Details of students")
        self.name=name
        self.age=age

s1=Student("mohsin",29)
print(f"name is :{s1.name} and age : {s1.age}")