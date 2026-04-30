SELECT
  sender_id
  ,COUNT(1)       AS count_messages
FROM messages
WHERE 
  sent_date >= '2022-08-01'
  AND sent_date < '2022-09-01'
GROUP BY sender_id
ORDER BY 
  count_messages DESC
LIMIT 2
