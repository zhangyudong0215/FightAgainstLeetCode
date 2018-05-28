-- Write your MySQL query statement below
select t2.Request_at as `Day`, round(count(if(t2.Status != 'completed', TRUE, NULL)) / count(*), 2) as `Cancellation Rate`
from (
    select t1.Status as `Status`, t1.Request_at as `Request_at`
    from Trips t1
    where t1.Client_Id not in (select Users_Id from Users where Banned = 'Yes') 
        and t1.Driver_Id not in (select Users_Id from Users where Banned = 'Yes')
    ) t2
where t2.Request_at between '2013-10-01' and '2013-10-03'
group by t2.Request_at
;
