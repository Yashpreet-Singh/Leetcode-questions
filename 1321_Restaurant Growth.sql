-- Write your PostgreSQL query statement below

-- combining same year amounts
with cte as(
    select visited_on, sum(amount) as sum_amount 
    from customer
    group by visited_on
)

select visited_on, 
sum(sum_amount) over(order by visited_on rows between 6 preceding and current row) as amount,
round(avg(sum_amount) over(order by visited_on rows between 6 preceding and current row),2) as average_amount
from cte
order by visited_on
offset 6
