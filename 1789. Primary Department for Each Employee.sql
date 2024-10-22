# Write your MySQL query statement below


select e.employee_id, 
case   
    when count(e.primary_flag)>1 then (select e2.department_id from employee as e2 where e2.primary_flag = 'Y' and e.employee_id=e2.employee_id)
    else e.department_id
end as department_id
from employee as e
group by e.employee_id
