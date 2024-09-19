-- Write your PostgreSQL query statement below

select sell_date, count(distinct(product)) as num_sold, string_agg(distinct product,',') as products
from activities
group by sell_date

------------------mysql

select sell_date, count( DISTINCT product ) as num_sold ,
    
    GROUP_CONCAT( DISTINCT product order by product ASC separator ',' ) as products --default separtoe in mysql is ','
    
        FROM Activities GROUP BY sell_date order by sell_date ASC;
