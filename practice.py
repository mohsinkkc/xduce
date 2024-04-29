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
#==========================================class method =======================================================


class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

c1=Student("mohsin",26)
print(c1.name,c1.age)

#1)Single

class Car:
    @staticmethod
    def start():
        print("the car has been started..")
    @staticmethod
    def stop():
        print("the Car has been stop..")
class Toyota(Car):
    def __init__(self,name):
        self.name=name

c2=Toyota("fortuner")
c2.start()


#2)multi level Inheritance
class Car:
    @staticmethod
    def start():
        print("the car has start..")

    @staticmethod
    def stop():
        print("the car is stop ..")

class Toyota(Car):
    def __init__(self,type):
        self.type=type

class Prius(Toyota):
    def __init__(self,type,name):
        self.name=name
        super().__init__(type)
        super().start()


c3=Prius("Electric","fortuner")
c3.stop()

print(f"the car name is {c3.name} and the car type is {c3.type}")

#3)multiple Inheritance

class A:
    var="welcome to A"
class B:
    var2="welcome to B"
class C(A,B):
    var3="welcome To C"

c4=C()

print(c4.var)
print(c4.var2)
print(c4.var3)

#4) Data Abstraction
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


# acc_no=int(input("Enter the account number :"))
# balance=0
# c5=Account(acc_no,balance)
# credit_amount=int(input("enter the amount to Credited :"))
# debit_amount=int(input("enter the amount to be Debit:"))
# c5.credit(credit_amount)
# c5.debit(debit_amount)
# print(f"from the Account : {c5.acc_no} the Available Balance in your account is : {c5.get_balance()}")

#5) del the item
class Mango:
    def __init__(self,name):
        self.name=name

c6=Mango("Mohsin")
print(c6.name)
# del c6.name
# print(c6.name)

#6)private
class Me:
    def __hello(self):
        print("Hello Everyone ")

    def World(self):
        return self.__hello()

c7=Me()
c7.World()

#7)class method
class Student:
    name="Mohsin"
    @classmethod
    def changename(cls,name):
        cls.name=name

c8=Student()
print(c8.name)
c8.changename("devanshu")
print("the changed name is :",c8.name)


#8)__gt__()
class Func:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __gt__(self,c9):
        return self.price < c9.price

c10=Func("tea",25)
print(f"the name of item is:{c10.name} and price is :{c10.price}")

c9=Func("Biscut",50)
print(f"the name of item is :{c9.name} and the price is {c9.price}")

print(" Is c10 < c9 :",c10 < c9)

#============================================================ rock Paper scissor========================================================================== 
# import random

# user_win=0
# computer_win=0
# option=["rock","paper","scissor"]


# while True:
#     user_input=input("enter your option (rock /paper / scissor) or q to quit :")

#     if user_input == "q":
#         break
    
#     if user_input not in option:
#         continue

#     random_number=random.randint(0,2)

#     computer_pick=option[random_number]
#     print("the computer pick " ,computer_pick)

#     if user_input == "scissor" and computer_pick == "paper":
#         print("you won ")
#         user_win +=1
#     elif user_input == "rock" and computer_pick == "scissor":
#         print("you won")
#         user_win += 1

#     elif user_input == "paper" and computer_pick=="rock":
#         print("you won ")
#         user_win += 1
#     else:
#         print("computer win")
#         computer_win += 1

# print("you win",user_win ,"times")
# print("computer win",computer_win,"times")
# print("goodbye")


#==============================================================password Manager==========================================================
# from cryptography.fernet import Fernet

# master=input("Enter the Master Password :")

# def view():
#     with open('Account.txt','r') as f:
#         for line in f.readlines():
#             data=line.rstrip()
#             user, passw = data.split("|")
#             print("user :", user ," | password",passw)

# def add():
#     name=input("Enter the Account name :")
#     pswd=input("Enter the Password :")
#     with open('Account.txt','a') as f:
#         f.write(name + "|" + pswd + "\n" )

# while True:
#     a=int(input('''
#     welcome to Bank of World
#     enter your option
#     1)view Account
#     2)Add details
#     3)Quit
#     enter your option:'''))
#     if a==1:
#         view()
#     elif a==2:
#         add()
#     elif a==3:
#         print("Thank you Visit Again")
#         break
#     else:
#         print("Kindly Select the valid Option")
#         continue

#=======================================================6 pig Game==============================================================


# import random

# def roll():
#     min_val=1
#     max_val=6
#     roll=random.randint(min_val,max_val)

#     return roll

# while True:
#     player=input("enter the number of player between (2-4) :")
#     if player.isdigit():
#         player=int(player)
#         if 2 <= player <= 4:
#             break
#         else:
#             print("the palyer must in between 2-4")
#     else:
#         print("invalid details")

# max_score=25
# player_score=[0 for _ in range(player)]

# while max(player_score) < max_score:
#     for player_indx in range(player):
#         print("\nthe player", player_indx + 1," turn has started\n")
#         print("the player score is :", player_score[player_indx], "\n")
#         current_score = 0

#         while True:
#             should_roll=input("would you like to roll (y)?:")
#             if should_roll != "y":
#                 break

#             value = roll()
#             if value == 1:
#                 print("you rolled 1 ,Turn done")
#                 current_score += value
#                 break
#             else:
#                 current_score += value
#                 print("you rolled the value",value)

#             print("your score is :",current_score)

#         player_score[player_indx] += current_score
#         print("your total Score is :", player_score[player_indx])
            

# max_score = max(player_score)
# winning_idx = player_score.index(max_score)
# print("player number ",winning_idx+1,"is the winner with score is ",max_score)


#===========================================================import Data from website using selenium==================================================================
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# import time
# import pandas as pd

# url = "https://www.investing.com/holiday-calendar/"
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get(url)

# table=driver.find_element(By.ID,'holidayCalendarData')
# rows=driver.find_elements(By.TAG_NAME,'tr')

# columns=[]
# data=[]

# for row in rows:
#     cells=row.find_elements(By.TAG_NAME,'th') + row.find_elements(By.TAG_NAME,'td')
#     if len(cells)>0:
#         if not columns:
#             columns=[cell.text.strip() for cell in cells]
#         else:
#             data.append([cell.text.strip() for cell in cells])

# num_colmns=len(columns)
# data_rows=[row for row in data if len(row) == num_colmns]

# print(data_rows)

# pf=pd.DataFrame(data_rows, columns=columns)
# excel_file='Selenium_Holiday.xlsx'
# pf.to_excel(excel_file)

# print("the Data is Exported Successfully",excel_file ,"\n")

# print()

#===================================================Web scraping data using BS4==========================================================
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd


# url="https://www.investing.com/holiday-calendar/"

# response=requests.get(url)

# soup=BeautifulSoup(response.content,'html.parser')


# table=soup.find('table',{'id':'holidayCalendarData'})

# columns=[]
# data=[]

# for row in table.find_all('tr'):
#     cells=row.find_all(['th','td'])
#     if len(cells) > 0:
#         if not columns:
#             columns=[cell.text.strip() for cell in cells]
#         else:
#             data.append([cell.text.strip() for cell in cells])

# print(data)
# pf=pd.DataFrame(data, columns=columns)
# excel_file='Beautiful_Holiday.xlsx'
# pf.to_excel(excel_file)

# print("Your BeatifulSoap file has been Successfully Exported the Data to ",excel_file)


#=================================================== ACID PROPERTIES USING MYSQL=================================

import mysql.connector

# Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    username="root",
    password="XDuce@123",
    database="person"
)
cursor = conn.cursor()

# Create a table for demonstration
cursor.execute("CREATE TABLE IF NOT EXISTS transactions (id INT AUTO_INCREMENT PRIMARY KEY, amount DECIMAL(10, 2))")

def insert_transaction(amount):
    # Insert a transaction into the table
    sql = "INSERT INTO transactions (amount) VALUES (%s)"
    cursor.execute(sql, (amount,))
    conn.commit()
    print("Transaction inserted successfully.")

def read_transactions():
    # Read all transactions from the table
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    print("All Transactions:")
    for transaction in transactions:
        print(transaction)

def update_transaction(transaction_id, new_amount):
    # Update a transaction
    sql = "UPDATE transactions SET amount = %s WHERE id = %s"
    cursor.execute(sql, (new_amount, transaction_id))
    conn.commit()
    print("Transaction updated successfully.")

def delete_transaction(transaction_id):
    # Delete a transaction
    sql = "DELETE FROM transactions WHERE id = %s"
    cursor.execute(sql, (transaction_id,))
    conn.commit()
    print("Transaction deleted successfully.")

try:
    # Perform transactions
    amount=input("enter the amount :")
    insert_transaction(amount)
    read_transactions()
    id=input("enter the id :")
    update_amount=int(input("enter amount to be updated:"))
    update_transaction(id, update_amount)
    delete_item=int(input("enter the id to delete :"))
    delete_transaction(delete_item)
    read_transactions()

except Exception as e:
    print("Error:", e)

finally:
    # Close the database connection
    cursor.close()
    conn.close()

#=============================function using mysql==============================================================


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


#==============================Unit test===============================================================
import unittest

class Teststring(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('mohisn'.upper(),'MOHSIN')

    def test_isupper(self):
        self.assertTrue('MOHSIN'.isupper())
        self.assertFalse('Mohsin'.isupper())

if __name__=="__main__":
    unittest.main()



#========================================================================================

import pyodbc

DRIVER_name='SQL Server'
Server_name='Mohasin-DTS'
Database_name='master'

connection_string=f"""

driver={{{DRIVER_name}}};
server={Server_name};
database={Database_name};
Trusted_Connection=yes;
"""


try:
    connection = pyodbc.connect(connection_string)
    # connection.autocommit = True
    # connection.execute('create database company')
    print("Database created",connection)

except pyodbc.Error as ex:
    print("Connection failed:", ex)