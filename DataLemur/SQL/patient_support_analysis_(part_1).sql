SELECT 
  COUNT(policy_holder_id)
FROM
(SELECT
  policy_holder_id
  ,COUNT(call_date)       AS count_calls
FROM callers
GROUP BY policy_holder_id
HAVING COUNT(call_date) >= 3) t