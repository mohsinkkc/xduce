'''
ACID PROPERITIES : 

Atomicity : ALll changes to data must be perform successfully or not at all

Consistence : Data must be consistent before and after transcation

Isolated :No other can change the data while the transcation is running

Durable:The change made by transcation must be persist/Not changeable unless or until updated

'''

import mysql.connector
conn = mysql.connector.connect(

    host="localhost",
    username="root",
    password="XDuce@123",
    port="3306",
    database="company"
)

cursor=conn.cursor()
# Create a DATABASE 
cursor.execute("create database IF NOT EXISTS company")
# Create a table for demonstration
cursor.execute("CREATE TABLE IF NOT EXISTS transcation(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(70), age INT, salary DECIMAL(10, 2))")

def insert(name,age,salary):
    # Insert a transaction into the table
    insert="insert into transcation (name,age,salary) values (%s,%s,%s)"
    cursor.execute(insert,(name,age,salary))
    conn.commit()
    print("Transcations insereted Successfully")

def read():
    # Read all transactions from the table
    read="select * from transcation"
    cursor.execute(read)
    trans=cursor.fetchall()
    print("\nThe All Transcation \n")
    for i in trans:
        print(i)

def update(id,new_value):
    # Update a transaction
    update=f"update transcation set salary={new_value} where id = {id}"
    cursor.execute(update)
    conn.commit()
    print("update Successfull")

def update_name(id,new_name):
    up="update transcation set name=%s where id=%s"
    cursor.execute(up,(new_name,id))
    print("The name has been Updated successfully")

def delete(id):
    # Delete a transaction
    delete="delete from transcation where id=%s"
    cursor.execute(delete,(id,))
    print("Deleted Successfully")

while True:
    print('''
                    please Select your option:

        1) To insert the data select 1
        2) To Fetch the data select 2
        3) To update the salary select 3
        4) update the name select 4
        5) Delete name select 5 
        6)Exit

    ''')
    Option=input("Enter your option :")

    if Option.isdigit():
        Option=int(Option)
        if Option ==1:
            name=input("Enter the name to be insert :")
            age=int(input("Enter your Age :"))
            salary=int(input("Enter the Salary :"))
            insert(name,age,salary)
        elif Option==2:
            read()
        elif Option==3:
            id=int(input("enter the id :"))
            new_value=int(input("enter the new salary amount to be update:"))
            update(id,new_value)
        elif Option==4:
            id=int(input("Enter the id to be updated :"))
            new_name=input("Enter the name : ")
            update_name(id,new_name)
        elif Option==5:
             id=int(input("Enter the id to be deleted :"))
             delete(id)
        else:
            break
    else:
        print("\nInvalid Option ! Kindly select the Valid Option")

cursor.close()
conn.close()
