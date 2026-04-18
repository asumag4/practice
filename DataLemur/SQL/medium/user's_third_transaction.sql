SELECT
  user_id
  ,spend
  ,transaction_date
FROM
(SELECT 
  *
  ,ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY transaction_date
  )   AS row_num
FROM transactions
ORDER BY 
  user_id
  ,row_num)
t
WHERE row_num = 3