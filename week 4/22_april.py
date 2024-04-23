#====================================SQL=================================================================================
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    username="root",
    password="XDuce@123",
    database="collage",
    port="3306"

)

cursor = connection.cursor()

#To create Database
# cursor.execute("create database collage")

#To create table
# cursor.execute("create table student (id int primary key,name varchar(30) )")

#To Insert The data into table
# cursor.execute(
#     '''
#     insert into student (id,name)
#     values(101,'mohsin'),
#     (102,'devanshu'),
#     (103,'Faizan'),
#     (104,'kaif')
#     '''
# )


query = "SELECT * FROM student"

cursor.execute(query)

# To fetch all data
rows = cursor.fetchall()

for row in rows:
    print(row)

#================================UPDATE=========================================

# update_query = "UPDATE student SET name = %s WHERE id = %s "

# # Define values to be updated
# new_value = "dev"
# condition_value = 101
#cursor.execute(update_query, (new_value, condition_value))

#=========================DELETE===================================================

# delete="DELETE * FROM collage.student WHERE id = 102"
# cursor.execute(delete)

#=====================ALTER=======================================================

# alter="ALTER TABLE collage.student ADD COLUMN  age int default=19"
# cursor.execute(alter)

result=cursor.fetchall()

for i in result:
    print(i)
# Execute the update query


# Commit the changes
connection.commit()

cursor.close()
connection.close()
# print(connection)







#to create Database
'''
create database collage;
use collage;
'''
# to Create table 
'''
create table student(
id int primary key,
name varchar(80),
marks int ,
grade char(1),
city varchar(30));
'''

#To insert into table
'''

insert into student(
id,name,marks,grade,city)
values(1,'mohsin',96,'A','Pune'),
(2,'devanshu',78,'C','Mumbai'),(3,'dev',85,'B','Mumbai'),(4,'Faizan',93,'A','Delhi'),(5,'Harsh',12,'F','Delhi'),(6,'dhruv',82,'B','Delhi');
'''

# To check all item from table

# select * from student;

# to check ,to delete , update and ordering form

#=======================ORDER BY==================================
'''
select city,avg(marks) from student
GROUP BY city 
order by city asc;

SET SQL_SAFE_UPDATES = 0;

#=======================UPDATE========================================
UPDATE student
SET grade="O" 
WHERE grade = 'A';

SELECT * FROM student;

#=========================DELETE========================================

DELETE FROM student
where marks < 30;

select * from student;

create table dept(
id int primary key,
name varchar(50));

create table teacher(
id int primary key,
name varchar(50),
dept_id int,
foreign key (dept_id) references dept(id)
on update cascade
on delete cascade
);

insert into dept
values(101,'maths'),(102,'english'),(103,'IT');

select * from dept;

insert into teacher
values(1,"sunny",102),(2,"Honey",101),(3,"zaheer",103),(4,"subham",102);

select * from teacher;

update dept
set id=105
where id = 102;

#===========================ALTER=============================================

alter table student
add column age int not null default=19;

select * from student;

#==================DROP==========================================================

alter table student
drop column age ;

alter table student 
change column  city address varchar(50);

alter table student
modify column grade varchar(10);

truncate table student;

drop table student;
drop table teacher;
drop table dept;

'''









