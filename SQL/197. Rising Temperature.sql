-- Write your MySQL query statement below
select w1.Id Id
from Weather w1 inner join Weather w2 on datediff(w1.RecordDate, w2.RecordDate) = 1
where w1.Temperature > w2.Temperature
;
