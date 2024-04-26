use company;

create table if not exists tbEmployee (id int primary key auto_increment,emp_id int ,first_name varchar(80),last_name varchar(70),salary decimal(10,2),joinig_date date,department varchar(80));

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

select ucase(first_name) from tbEmployee;

select substring(first_name,1,3) from tbEmployee;
 
select first_name,replace(first_name,'A','a') from tbEmployee;

select * from tbEmployee
where salary >=5000 or salary <=10000;

select count(first_name) from tbEmployee
where department = "admin";

select * from tbEmployee
where first_name like '%A%';

create table clone_employee like tbEmployee;

select salary from tbEmployee
order by salary asc limit 10;

create table clone_employee_data as select * from tbEmployee;

select salary from tbEmployee
order by salary limit 3,1;

select emp_id , count(emp_id) from tbemployee
group by emp_id
having count(emp_id)>1;

