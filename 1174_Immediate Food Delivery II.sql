-- Write your PostgreSQL query statement below

--https://datalemur.com/sql-tutorial/sql-division (float divisions)

with cte as(
    select *,
        case 
            when customer_pref_delivery_date = order_date then 'immediate'
            else 'scheduled'
        end as category
    from delivery
),cte2 as(
    select *,
    row_number() over (partition by customer_id order by order_date) as rank
    from cte
    )

select  ROUND((SUM(case when category='immediate' then 1 else 0 end) * 100.0/ count(*)  ),2) as immediate_percentage
from cte2
where rank=1 


--much easier solution 
select
    round(avg(case when order_date=customer_pref_delivery_date then 1 else 0 end)*100, 2) as immediate_percentage
from
    Delivery
where
    (customer_id, order_date) in (
        select 
            customer_id, min(order_date)
        from
            Delivery
        group by customer_id
    )
