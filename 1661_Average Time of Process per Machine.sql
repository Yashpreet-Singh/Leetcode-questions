-- Write your PostgreSQL query statement below

with cte as(
select machine_id, max(timestamp) - min(timestamp) as processing_time
from activity
group by machine_id,process_id       )

select machine_id, round(cast(avg(processing_time)as numeric) ,3) as processing_time  ---no need for cast in Mysql
from cte
group by machine_id
