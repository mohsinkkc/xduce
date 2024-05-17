-- Questions
-- 1) List all students who are subject in 'Computer Science'.
-- 2) Find the total number of students in the table.
-- 3) Retrieve the names of students who are older than 21.
-- 4) Get the average age of students subject in 'Biology'.
-- 5) Find the student with the highest age.
-- 6) List all unique subject from the student table.
-- 7) Update the major of the student named 'Alice Johnson' to 'Astronomy'.
-- 8) Delete the record of the student whose id is 5.
-- 9) Count the number of students in each major.
-- 10) Add a new student named 'Tom Hanks', aged 24, subject in 'Theater'.

--  Intermediate Questions
-- 11) Retrieve the full names of students and their subject, ordered by their last names in ascending order.
-- 12) Find the average age of students grouped by their subject.
-- 13) Get the details of students who are the youngest in each major.
-- 14) List students who have a last name starting with the letter 'J'.
-- 15) Retrieve the second oldest student in the table.
-- 16) Update the ages of all students, adding one year to each student's age.
-- 17) List all students who are subject in either 'Computer Science' or 'Mathematics'.
-- 18) Find students whose first name is exactly four characters long.
-- 19) Retrieve students who are not subject in 'History' or 'Art'.
-- 20)Delete all students who are older than 23 years.

-- Create the student table
CREATE TABLE student (
    id INT IDENTITY(1,1) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    subject VARCHAR(100)
);

-- Insert 15 values into the student table
INSERT INTO student (first_name, last_name, age, subject) VALUES
('John', 'Doe', 20, 'Computer Science'),
('Jane', 'Smith', 22, 'Biology'),
('Alice', 'Johnson', 19, 'Physics'),
('Bob', 'Brown', 21, 'Mathematics'),
('Carol', 'Davis', 23, 'Chemistry'),
('Dave', 'Wilson', 20, 'Engineering'),
('Eve', 'Taylor', 22, 'Economics'),
('Frank', 'Anderson', 21, 'Philosophy'),
('Grace', 'Thomas', 19, 'History'),
('Hank', 'Moore', 20, 'Political Science'),
('Ivy', 'Jackson', 22, 'Sociology'),
('Jack', 'Martin', 21, 'Literature'),
('Karen', 'Lee', 23, 'Art'),
('Leo', 'White', 19, 'Psychology'),
('Mona', 'Harris', 20, 'Music');


-- 1) List all students who are majoring in 'Computer Science'.
SELECT * from student
WHERE subject='Biology';

-- 2) Find the total number of students in the table.
SELECT COUNT(*) from student;

-- 3) Retrieve the names of students who are older than 21.

SELECT * from student
WHERE age > 21;

-- 4) Get the average age of students majoring in 'Biology'.
SELECT AVG(age)  from student
WHERE subject='Biology';

-- 5) Find the student with the highest age.
SELECT MAX(age) FROM student;
-- 6) List all unique subject from the student table.
SELECT distinct(subject) from student;

-- 7) Update the major of the student named 'Alice Johnson' to 'Astronomy'.
UPDATE student
SET first_name ='Astronomy'
WHERE first_name='Alice'

-- 8) Delete the record of the student whose id is 5.

DELETE student
WHERE id=5

-- 9) Count the number of students in each Subject.
SELECT COUNT(id),subject from student
GROUP by subject;

-- 10) Add a new student named 'Tom Hanks', aged 24, majoring in 'Theater'.
INSERT INTO student (first_name, last_name, age, subject) VALUES ('Tom', 'Hanks', 24, 'Theater');


--  Intermediate Questions

-- 11) Retrieve the full names of students and their subject, ordered by their last names in ascending order.

SELECT CONCAT(first_name,' ',last_name) as full_name,subject From student
ORDER by last_name ASC;

-- 12) Find the average age of students grouped by their subject.
SELECT AVG(age),subject FROM student
GROUP BY subject;

-- 13) Get the details of students who are the youngest in each major.
SELECT MIN(age),subject FROM student
GROUP by subject;

-- 14) List students who have a last name starting with the letter 'J'.

SELECT * FROM student
WHERE  last_name like 'J%';

-- 15) Retrieve the second oldest student in the table.


SELECT * 
FROM student 
ORDER BY age DESC 
OFFSET 1;


-- 16) Update the ages of all students, adding one year to each student's age.
UPDATE student 
SET age = age + 1;

-- 17) List all students who are subject in either 'Computer Science' or 'Mathematics'.

SELECT * from student
WHERE subject IN ('Computer Science','Mathematics');

-- 18) Find students whose first name is exactly four characters long.

SELECT * FROM student
WHERE LEN(first_name) = 4;

-- 19) Retrieve students who are not subject in 'History' or 'Art'.

SELECT * from student
WHERE subject NOT IN ('History','Art');

-- 20)Delete all students who are older than 23 years.

DELETE student
WHERE age > 23;

-- Advance 

-- 21) Find the most common major among students and the number of students in that major.

SELECT COUNT(*),subject from student
ORDER by subject DESC
limit 1:

-- 22)Retrieve the details of students who share the same first name as any other student.
-- 23)Calculate the difference in age between the youngest and the oldest student.
-- 24)Find students whose full names have more than 10 characters (considering both first and last names combined).
-- 25) List the students along with their rank based on their age, from oldest to youngest.
-- 26) Retrieve the top 3 youngest students for each major.
-- 27) Find the major with the highest average age and the corresponding average age.
-- 28) Identify students who have the same last name as any other student but a different first name.
-- 29) Calculate the cumulative age of students ordered by their first name.
-- 30) Find the student(s) who have the second highest age in the entire table.



SELECT * FROM student;