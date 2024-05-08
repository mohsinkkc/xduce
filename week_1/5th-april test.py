# Todays Test:
# Suppose you are building a system to manage student grades. # Implement a Python program that includes the following functionalities:
# 1. A function to add a new student with their grades.
# 2. A function to calculate the average grade of a student.
# 3. A decorator function to ensure that Student is pass or fail in exam
# 4. A function to retrieve the highest grade among all students.
# 5. A function to retrieve the average grade of all students.
# Constraints: - Use dictionaries to store student names as keys and their grades as values.

#=================================function to add students=========================

'''def decorator(funct):
    def wrapper():
        if grade > 5:
            print("the number is fail")
        else:
            print("good")
        funct
    return wrapper'''

student={}
while True:
    def add_student(student,name,grade):
                student[name] = grade
                return student


    name = input("enter the name :")
    grade = int(input("enter the grade out of (10):"))
    print(add_student(student,name, grade))

    print("do you want to continue \n")
    z=input("enter your choice y/n:")
    if z == 'y':
        continue
    else:
        break

def average(student):
            total=sum(student.values())
            avg_grade=total/len(student)
            print("the average is :",avg_grade)

def highest(student):
       high_mark=max(student.values())
       print("the highest grade is :",high_mark)


def main():
       average(student)
       highest(student)

if __name__=='__main__':
       main()










    

