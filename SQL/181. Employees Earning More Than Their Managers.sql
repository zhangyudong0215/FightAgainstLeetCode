-- Write your MySQL query statement below
select e.Name as Employee
from Employee e
where e.ManagerId is not null and e.Salary > (select Salary from Employee where Id = e.ManagerId)
;
