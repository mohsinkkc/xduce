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
        3) To update the Data select 3
        4) Delete the Data select 4
        5) EXIT
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
            id="Enter the id to be deleted :"
            delete(id)
        else:
            break
    else:
        print("\nInvalid Option ! Kindly select the Valid Option")
