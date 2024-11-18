# Write your MySQL query statement below

-- SELECT 
--     CASE 
--         WHEN EXISTS (SELECT num FROM mynumbers GROUP BY num HAVING count(num) = 1)
--         THEN (SELECT num FROM mynumbers GROUP BY num HAVING count(num) = 1 ORDER BY num DESC LIMIT 1)
--         ELSE NULL
--     END AS num;

SELECT COALESCE(
    (SELECT num FROM mynumbers GROUP BY num HAVING count(num) = 1 ORDER BY num DESC LIMIT 1), 
    NULL
) AS num;
