#mysql
select *
from patients
#where conditions ~ '\mDIAB1' 
where conditions REGEXP  '^(.*\\s)?DIAB1'
