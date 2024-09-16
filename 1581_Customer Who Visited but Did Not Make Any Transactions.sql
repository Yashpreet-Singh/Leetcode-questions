-- Write your PostgreSQL query statement below

select customer_id , count(visit_id) as count_no_trans
from visits
where (customer_id,visit_id) not in 
(select customer_id,visit_id
from visits v
join transactions t using(visit_id))
group by customer_id
