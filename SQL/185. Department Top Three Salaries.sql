# Write your MySQL query statement below
select d.Name `Department`, e.Name `Employee`, e.Salary `Salary`
from Employee e inner join Department d on e.DepartmentId = d.Id
where 3 > (select count(distinct ee.Salary) from Employee ee where ee.Salary > e.Salary and ee.DepartmentId = e.DepartmentId)
;
