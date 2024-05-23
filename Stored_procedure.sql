CREATE PROCEDURE newstudent2
as SELECT * from student
GO;

EXEC newstudent2;

drop procedure stu1;

CREATE PROCEDURE stu1 @subject VARCHAR(55)
as SELECT * from student WHERE subject=@subject ;

EXEC stu1 @subject ='Theater';

CREATE PROCEDURE stu3 @subject VARCHAR(55),@age INT
as SELECT * FROM student WHERE subject=@subject AND age=@age;

EXEC stu3 @subject='Theater',@age=24 ;

CREATE FUNCTION fn_getdata(@subject varchar(55))
RETURNS TABLE
as RETURN
(
    SELECT * from student WHERE subject=@subject
)
GO

create index indx_name on student(subject);

SELECT * FROM fn_getdata('Philosophy');
GO


select * from student;
GO