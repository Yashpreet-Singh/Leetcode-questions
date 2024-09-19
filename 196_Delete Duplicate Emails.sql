-- Write your PostgreSQL query statement below


delete from person
where id not in (
select min(id)
from person
group by email
)

-------------------------------sql

DELETE p1
FROM Person p1, Person p2
WHERE p1.Email = p2.Email AND
p1.Id > p2.Id
