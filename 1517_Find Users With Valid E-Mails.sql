# Write your MySQL query statement below  https://www.scaler.com/topics/regex-in-sql/

select *
from users
where trim(mail) REGEXP '^[A-Za-z]{1}[A-Za-z0-9\._-]*@leetcode[.]com$'
