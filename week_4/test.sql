use company;
-- q1 : create Table
create table if not exists tbEmployee (id int primary key auto_increment,emp_id int ,first_name varchar(80),last_name varchar(70),salary decimal(10,2),joinig_date date,department varchar(80));
-- q2:insert data into table
INSERT INTO tbEmployee (emp_id, first_name, last_name, salary, joinig_date, department) VALUES 
(1, 'Mohmad', 'Mohasin', 50000, '2024-05-01', 'Manager'),
(2, 'Devanshu', 'Chauhan', 75000, '2024-05-02', 'Executive'),
(3, 'Ankita', 'Patel', 90000, '2024-05-01', 'Manager'),
(2, 'Faizan', 'Mansuri', 85000, '2024-05-02', 'Lead'),
(1, 'Shivam', 'Jani', 300000, '2024-05-01', 'Executive'),
(4, 'Dhruv', 'Rathi', 400000, '2024-05-03', 'Lead');

INSERT INTO tbEmployee (emp_id, first_name, last_name, salary, joinig_date, department) VALUES 
(1, 'shivam', 'mavi', 5000, '2024-05-11', 'jr.Manager'),
(2, 'Rohit', 'sharma', 85000, '2024-05-22', 'sr.Executive'),
(9, 'Amit', 'Mishra', 92000, '2024-05-18', 'Manager'),
(8, 'Amir', 'Mansuri', 32000, '2024-05-21', 'sr.Lead'),
(1, 'Shivam', 'dube', 30000, '2024-05-01', 'Executive'),
(7, 'Dhruv', 'shah', 40000, '2024-05-06', 'Lead');

select*from tbEmployee;
-- Q3 : display name in Upper Case
select ucase(first_name) from tbEmployee;
-- Q4 : display only first three letter only
select substring(first_name,1,3) from tbEmployee;
 -- Q5 :Replace A with a
select first_name,replace(first_name,'A','a') from tbEmployee;
-- Q6 : find the Salary >=5000 and salary <=10000
select  * from tbemployee
where salary >=5000 or salary <=10000;

-- Q7: cloning new table from table
create table clone_employee like tbEmployee;

-- Q8 : details of worker whose first name contain a
select * from tbEmployee
where first_name like '%A%';
-- Q9 : count of employee working in department admin
select count(first_name) from tbEmployee
where department = "admin";
-- Q10 : current date
select curdate();

-- Q11 : ten number of highest salary
select salary from tbEmployee
order by salary asc limit 10;
-- Q12: create new table from table with its data and structure
create table clone_employee_data as select * from tbEmployee;
-- Q13 : 3rd higest value
select salary from tbEmployee
order by salary limit 2,1;
-- Q14 : retrive Duplicate value
select emp_id , count(emp_id) from tbemployee
group by emp_id
having count(emp_id)>1;


select * from tbemployee
limit 2;