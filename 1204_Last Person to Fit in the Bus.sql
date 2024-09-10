-- Write your PostgreSQL query statement below


select person_name
from
(select person_name,
sum(weight) over (order by turn asc) as total_weight
from queue)
where total_weight <=1000
order by total_weight desc
limit 1


-- Advance Joins (joins all the turn like (1):1, (2):12, (3):123)
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1
