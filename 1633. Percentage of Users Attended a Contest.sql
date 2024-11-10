# Write your MySQL query statement below

select r.contest_id, round(count(r.user_id) *100/ (select count(distinct(user_id)) from users),2) as percentage
from register r
join users u on r.user_id = u.user_id
group by contest_id 
order by percentage desc, r.contest_id asc

