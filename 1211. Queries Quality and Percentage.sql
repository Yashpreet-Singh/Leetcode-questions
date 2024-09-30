
# Write your MySQL query statement below


select query_name, ROUND(AVG(rating/position),2) as quality, Round(SUM(IF(rating<3,1,0)) * 100/ Count(rating),2) as poor_query_percentage
from queries
group by query_name
having query_name is not null
