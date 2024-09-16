-- Write your PostgreSQL query statement below

select customer_id , count(visit_id) as count_no_trans
from visits
where (customer_id,visit_id) not in 
(select customer_id,visit_id
from visits v
join transactions t using(visit_id))
group by customer_id

  -----------------------------------------------------using left join

SELECT v.customer_id, COUNT(v.visit_id) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;
