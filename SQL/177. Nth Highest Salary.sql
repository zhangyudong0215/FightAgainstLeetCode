CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      ifnull((
          select distinct Salary
          from Employee
          order by Salary desc
          limit M, 1
        ), null)
  );
END
