-- Write your MySQL query statement below
select s1.Score, (select count(distinct Score) from Scores where Score >= s1.Score) Rank
from Scores S1
order by Rank
;
