SELECT ROUND(SUM(CASE WHEN event_date - first_login = 1 THEN 1 ELSE 0 END)::numeric / COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT player_id, event_date,
           MIN(event_date) OVER(PARTITION BY player_id) AS first_login
    FROM Activity) p
