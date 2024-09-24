-- Write your PostgreSQL query statement below


select su.user_id, round(cast(avg(
case
    when action= 'confirmed' then 1
    else 0 --for null as well
end) as numeric),2) as confirmation_rate
from signups su
left join confirmations c
on su.user_id=c.user_id
group by su.user_id

--------------------------mysql

# Write your MySQL query statement below
select s.user_id, round(avg(if(c.action="confirmed",1,0)),2) as confirmation_rate
from Signups as s left join Confirmations as c on s.user_id= c.user_id group by user_id;

