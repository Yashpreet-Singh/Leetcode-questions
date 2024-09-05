-- Write your PostgreSQL query statement below

--for even lag , get prev item in column
--for odd lead, gets next item in column
select id,
case 
    when MOD(id,2)=0 then lag(student,1) over(order by id) 
    else COALESCE(lead(student,1) over(order by id),student)
end as student
from seat


--solution2
SELECT
ROW_NUMBER() OVER(order by IF(MOD(id, 2) = 0, id-1, id+1) ) as id,
student
FROM seat
