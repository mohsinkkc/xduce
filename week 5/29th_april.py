# pip install pyodbc
# import pyodbc 
# create a connection 
import pyodbc

try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                                    'Server=MOHASIN-DTS;'
                                    'Database=company;'
                                    'Trusted_Connection=yes;'
                                    'uid=sa;'
                                    'psw=XDuce@123'
                                )
    
    # ds = connection.cursor()
    # all='select * from employee'
    # ds.execute(all)
    # row = ds.fetchall()

    # for i in row:
    #     print(i)
    # conn.commit()
    print("database created")

except pyodbc.Error as ex:
    print("Connection failed:", ex)


# conn=('Driver={ODBC Driver 17 for SQL Server};',
#                     'Server=MOHASIN-DTS;',
#                     'Database=company',
#                     'Trusted_Connection=yes'
#                     )

# connection=pyodbc.connect(conn)
# cursor=connection.cursor()
# cursor.execute("SELECT * FROM employee")

# for i in cursor:
#     print(i)

# cursor.commit()
# print("database connected")




