# Write your MySQL query statement below
select name, population, area
from World
where area > 3e6 or population > 2.5e7
;