-- Write your PostgreSQL query statement below

select distinct(num) as ConsecutiveNums
from
(select num,
lead(num,1) over() as lead_column1,
lead(num,2) over() as lead_column2
from logs) as subquery
where num = lead_column1 and lead_column1 =lead_column2


  --using joins
select distinct(lg1.num) as ConsecutiveNums
from logs lg1
join logs lg2 on lg1.num = lg2.num and lg2.id = lg1.id + 1
join logs lg3 on lg2.num = lg3.num and lg3.id = lg2.id + 1
