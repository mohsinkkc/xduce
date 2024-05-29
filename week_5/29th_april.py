import pyodbc
import pandas as pd

server_name=r'MOHASIN-DTS'
database_name='company'
username='sa'
password='XDuce@123'

try:
    conn=f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server_name};DATABASE={database_name};uid={username};pwd={password}'

    connection=pyodbc.connect(conn)
    print('connected')
    cursor=connection.cursor()

    # cursor.execute("INSERT INTO employee (id,name) VALUES (5,'dhruv'),(6,'kkc')")

    query = cursor.execute("SELECT * FROM employee;")
    data = query.fetchall()
    
    delete = "DELETE FROM employee WHERE id = 5"
    cursor.execute(delete)
    connection.commit()
    print("Data deleted Successfully")
    

    update="UPDATE employee set name='dev' where id=6 "
    cursor.execute(update)
    connection.commit()
    print("Data has updated successfully ")

    print(data)
    connection.commit()
    print('Data Fetch Successfully')

except Exception as e:
    print("ERROR :",e)


