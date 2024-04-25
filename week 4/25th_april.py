import mysql.connector


conn = mysql.connector.connect(

    host="localhost",
    username="root",
    password="XDuce@123",
    port="3306",
    database="company"
)

cursor=conn.cursor()

cursor.execute("create database IF NOT EXISTS company")

cursor.execute("CREATE TABLE IF NOT EXISTS transcation(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(70), age INT, salary DECIMAL(10, 2))")

# def insert(name,age,salary):
#     a="insert into transcation (name,age,salary) values (%s,%s,%s)"
#     cursor.execute(a,(name,age,salary))
#     conn.commit()
#     print("Transcations insereted Successfully")

# def read():
#     b="select * from transcation"
#     cursor.execute(b)
#     trans=cursor.fetchall()
#     print("The All Transcation")
#     for i in trans:
#         print(i)

# def update(id,new_value):
#     c=f"update transcation set salary={new_value} where id = {id}"
#     cursor.execute(c)
#     conn.commit()
#     print("update Successfull")

# def delete(id):
#     d="delete from transcation where id=%s"
#     cursor.execute(d,(id,))
#     print("Deleted Successfully")

# while True:
#     '''
#     please Select your option:
#     1) To insert the data 
#     2) To Fetch the data
#     3) To update the Data
#     4) Delete the Data
#     5) EXIT
#     '''
#     Option=input("Enter your option :")

#     if Option.isdigit():
#         Option=int(Option)
#         if Option ==1:
#             name=input("Enter the name to be insert :")
#             age=int(input("Enter your Age :"))
#             salary=int(input("Enter the Salary :"))
#             insert(name,age,salary)
#         elif Option==2:
#             read()
#         elif Option==3:
#             id=int(input("enter the id :"))
#             new_value=int(input("enter the new salary amount to be update:"))
#             update(id,new_value)
#         elif Option==4:
#             id="Enter the id to be deleted :"
#             delete(id)
#         else:
#             break
#     else:
#         print("Enter the Valid Option")

def insert(name,age,salary):
    insert="insert into transcation(name,age,salary) values (%s,%s,%s)"
    cursor.execute(insert,(name,age,salary))
    print("Inserted Successfully")

def read():
    read="select * from transcation"
    cursor.execute(read)
    trans=cursor.fetchall()
    print("Transcation details are : \n")
    for i in trans:
        print(i)

def update(id,new_amount):
    update="update transcation set salary= %s where id=%s"
    cursor.execute(update,(new_amount,id))
    print("Updated successfully")

def delete(id):
    delete="delete from transcation where id=%s"
    cursor.execute(delete,(id,))
    print("Info Deleted Successfully")

while True:
    print('''
            Please Select your option

     1) To insert the data 
     2) To Fetch the data
     3) To update the Data
     4) Delete the Data
     5) EXIT
    
    ''')
    option=input("select Your option from (1-5):")
    if option.isdigit():
        option=int(option)
        if option == 1:
            name=input("Enter name to be Inserted :")
            age=int(input("enter the Age :"))
            salary=int(input("Enter the salary :"))
            insert(name,age,salary)
        elif option==2:
            read()
        elif option==3:
            id=int(input("Enter id:"))
            new_amount="Enter the new amount:"
            update(id,new_amount)
        elif option==4:
            id=int(input("Enter id:"))
            delete(id)
        else:
            break
    else:
        print("Invalid Key word ! , please enter valid option")