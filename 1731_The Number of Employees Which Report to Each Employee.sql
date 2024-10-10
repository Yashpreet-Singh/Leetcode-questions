select e1.employee_id, e1.name, count(e0.reports_to) as reports_count, round(avg(e0.age)) as average_age from employees e0
join employees e1
on  e1.employee_id = e0.reports_to
group by e0.reports_to
order by e1.employee_id
