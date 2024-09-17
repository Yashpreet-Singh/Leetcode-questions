select w2.id as id
from weather w1
join weather w2 on w1.recordDate + INTERVAL '1 days' = w2.recordDate  --or 1 day
where w2.temperature > w1.temperature
order by w1.recordDate asc

---------------------------------------

SELECT current_day.id
FROM Weather AS current_day
WHERE EXISTS (
    SELECT 1
    FROM Weather AS yesterday
    WHERE current_day.temperature > yesterday.temperature
    AND current_day.recordDate = yesterday.recordDate + 1
);
