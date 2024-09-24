select p.product_name, sum(o.unit) as unit
from products p 
join orders o on p.product_id = o.product_id
where extract('year' from o.order_date) = 2020 and extract('month' from o.order_date) = 2   --mysql (WHERE YEAR(o.order_date)='2020' AND MONTH(o.order_date)='02')
group by p.product_name
having sum(o.unit)>=100
