-- Write your PostgreSQL query statement below


with cte as(

select *,
dense_rank() over(partition by product_id order by change_date desc) as rank
from products
where change_date <= '2019-08-16')

select product_id,new_price as price
from cte 
where rank=1

union

select distinct product_id, 10 as price 
from products
where product_id not in (select product_id from cte)



