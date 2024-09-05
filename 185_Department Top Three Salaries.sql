-- Write your PostgreSQL query statement below

with cte as(
select e.*,d.name as Department
from employee e
join department d on d.id = e.departmentId)


select Department,name as Employee, salary
from ( select *,
DENSE_RANK() over(PARTITION BY departmentId order by salary desc) as topdesc
from cte)
where topdesc <= 3;
