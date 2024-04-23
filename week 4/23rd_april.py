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
cursor.execute("CREATE TABLE IF NOT EXISTS student.teacher (id int primary key, salary int) ")

# print("the TABle has created Successfully :",)

# cursor.execute("""
# INSERT INTO IF NOT EXISTS student.students (id,name,marks,subject)
# VALUES(101,'mohsin',95,'maths'),
#     (102,'devanshu',82,'english'),
#     (103,'faizan',54,'hindi'),
#     (104,'harsh',78,'maths')

# """)

# cursor.execute("""

# INSERT INTO student.teacher(id,salary)
# VALUES(101,35000),
# (106,45000),(103,32000),(108,56440),(102,120000)

# """)
# cursor.execute("INSERT INTO student.teacher VALUE (109,61000)")


# ex = "SELECT * FROM student.teacher"
# cursor.execute(ex)
# teachers = cursor.fetchall()
# # print(teachers)

# for i in teachers:
#     print(i)  


# query="SELECT * FROM student.students"
# cursor.execute(query)
# rows = cursor.fetchall()

# cursor.execute("UPDATE student.students SET marks = marks-20 WHERE subject='maths' ")

# cursor.execute("DELETE FROM student.students WHERE marks < 60")
# cursor.execute("ROLLBACK")

# for row in rows:
#     print(row)

#==================================Inner Join===============================================================

# inner="SELECT * FROM student.students INNER JOIN student.teacher where student.students.id = student.teacher.id"
# cursor.execute(inner)

#=================================Left Join================================================================

# left = "SELECT * FROM student.students RIGHT JOIN student.teacher ON student.students.id = student.teacher.id"
# cursor.execute(left)

# ===============================Right Join================================================================
# right="SELECT * FROM student.teacher LEFT JOIN student.students ON student.teacher.id = student.students.id "
# cursor.execute(right)

#=============================FULL JOIN==================================================================================

# full_join="SELECT * FROM student.students RIGHT JOIN student.teacher ON student.students.id = student.teacher.id UNION SELECT * FROM student.teacher LEFT JOIN student.students ON student.students.id = student.teacher.id"
# cursor.execute(full_join)

#=========================================GROUP BY======================================================================
# group="SELECT name FROM student.students WHERE marks >=70 GROUP BY name"
# cursor.execute(group)

#======================================ORDER BY========================================================================

order="SELECT * FROM student.students ORDER BY name"
cursor.execute(order)
rst = cursor.fetchall()



for i in rst:
    print(i)

conn.commit()


cursor.close()
conn.close()


'''

create table student (
id int primary key,
name varchar(80));

create table course(
id int primary key ,
course varchar(50));

insert into student 
values (101,'mohsin'),(102,'devanshu'),(103,'Faizan'),(104,'kaif');

select * from student;

insert into course
values (101,'math'),(104,'physics'),(108,'english'),(109,'science');

select * from course;

select * from student
inner join course
on student.id=course.id;

select * from student
left join course
on student.id=course.id;

select * from course
right join student
on student.id=course.id;


select * from student
left join course
on student.id=course.id
union
select * from course
right join student
on student.id=course.id;


create view view1 as select id,name from student;

select * from view1;
'''