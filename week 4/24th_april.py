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

# ds.execute("CREATE TABLE IF NOT EXISTS info (id int not null ,name varchar(60) primary key,mobile varchar(22) unique not null)")
# ds.execute("DROP TABLE subinfo")
# ds.execute("CREATE INDEX idx_name ON info(name)")
#================================================================Forieng Key AND PRIMARY KEY========================================================================

# ds.execute("CREATE TABLE IF NOT EXISTS subinfo (id int AUTO_INCREMENT primary key, name varchar(60),salary int, FOREIGN KEY (name) references info(name) ON UPDATE CASCADE ON DELETE CASCADE) ")

# ds.execute("""
# INSERT INTO subinfo (name, salary)
# VALUES
#     ('mohsin', 46000),
#     ('sunny', 8510),
#     ('faizan', 25000)
# """)

subshow="SELECT * FROM subinfo"
ds.execute(subshow)
sub=ds.fetchall()

for i in sub:
    print(i)


# print("Insert data",ds.execute("""
# INSERT INTO info  (id,name,mobile)
# VALUES (1,'mohsin','7826541398'),
# (2,'devanshu','6354128715'),
# (3,'sunny','8745621987'),
# (4,'faizan','8759214568'),
# (5,'subham','9568741254')
# """))

# update="UPDATE info set name='devanshu' where name ='sunny'"
# ds.execute(update)
# res=ds.fetchall()

# for i in res:
#     print(i)

show="SELECT * FROM info"
ds.execute(show)
result=ds.fetchall()

# print(result)
for i in result:
    print(i)

conn.commit()

conn.close()
ds.close()


