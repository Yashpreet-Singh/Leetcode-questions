-- Write your PostgreSQL query statement below


with cte as (select mr.user_id,mr.movie_id,mr.rating,mr.created_at,u.name,m.title
from movierating mr
join users u on mr.user_id=u.user_id
join movies m on mr.movie_id=m.movie_id
)

(select name as results
from cte 
group by name,user_id
order by Count(*) desc,name asc
limit 1)
Union all
(select title
from cte 
where date_part('month',created_at) = 2 and date_part('year',created_at) = 2020 
group by movie_id,title
order by AVG(rating)  desc,title asc
limit 1)








