-- Write your MySQL query statement below
select P.FirstName, P.LastName, A.City, A.State
from Person P left join Address A on P.PersonId = A.PersonId
;
