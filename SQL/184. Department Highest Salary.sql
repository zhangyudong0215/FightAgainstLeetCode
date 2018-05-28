-- -- Write your MySQL query statement below
-- -- 这种方法为什么错了?
-- select d.Name as Department, e.Name as Employee, max(e.Salary) as Salary
-- from Employee as e inner join Department as d on e.DepartmentId = d.Id
-- group by e.DepartmentId
-- order by Salary
-- ;

SELECT b.Name AS Department, a.Name AS Employee, a.Salary
FROM Employee a JOIN Department b ON a.DepartmentId = b.Id
WHERE (a.DepartmentId, a.Salary) in
   (SELECT DepartmentId, Max(Salary) AS Salary
    FROM Employee
    GROUP BY DepartmentId
