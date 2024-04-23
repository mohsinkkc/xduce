import mysql.connector 

conn=mysql.connector.connect(
    host="127.0.0.1",
    username="root",
    password="XDuce@123",
    port="3306"
)

cursor=conn.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS student')

cursor.execute("""
CREATE TABLE IF NOT EXISTS student.students (
    id int primary key,
    name varchar(60),
    marks int,
    subject varchar(60)
);

""")

# cursor.execute("""
# INSERT INTO IF NOT EXISTS student.students (id,name,marks,subject)
# VALUES(101,'mohsin',95,'maths'),
#     (102,'devanshu',82,'english'),
#     (103,'faizan',54,'hindi'),
#     (104,'harsh',78,'maths')

# """)


query="SELECT * FROM student.students"
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.commit()

print(conn)

cursor.close()
conn.close()