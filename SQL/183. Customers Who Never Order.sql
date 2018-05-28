-- Write your MySQL query statement below
select C.Name Customers
from Customers C left join Orders O on C.Id = O.CustomerId
where O.Id is null
;
