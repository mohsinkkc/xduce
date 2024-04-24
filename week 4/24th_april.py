import mysql.connector

conn=mysql.connector.connect(

    host="localhost",
    username="root",
    password="XDuce@123",
    port="3306",
    database="person"
)

ds=conn.cursor()

# ds.execute("CREATE DATABASE IF NOT EXISTS person")

# ds.execute("CREATE TABLE IF NOT EXISTS info (id int primary key,name varchar(60),mobile varchar(22) unique not null)")
# ds.execute("DROP TABLE subinfo")
# ds.execute("CREATE INDEX idx_name ON info(name)")
# ds.execute("CREATE TABLE subinfo (id int, name varchar(50), salary int, PRIMARY KEY (id), FOREIGN KEY (id) REFERENCES info(id))")

ds.execute("""
INSERT INTO subinfo (id,salary)
values(1,46000),(2,8510),(6,84650),(7,25000)
""")

# subshow="SELECT * FROM subinfo"
# ds.execute(subshow)
# sub=ds.fetchall()

# for i in sub:
#     print(i)

# print("Insert data",ds.execute("""
# INSERT INTO info  (id,name,mobile)
# VALUES IF NOT EXISTS (1,'mohsin','7826541398'),
# (2,'devanshu','6354128715'),
# (3,'sunny','8745621987'),
# (4,'faizan','8759214568'),
# (5,'subham','9568741254')
# """))

show="SELECT * FROM info"
ds.execute(show)
result=ds.fetchall()

# print(result)
for i in result:
    print(i)

conn.commit()

conn.close()
ds.close()


