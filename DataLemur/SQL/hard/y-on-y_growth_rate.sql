WITH window1 AS (
SELECT
  product_id
  ,EXTRACT(YEAR FROM transaction_date)                AS yr
  ,spend
  ,RANK() OVER (
  PARTITION BY product_id
  ORDER BY EXTRACT(YEAR FROM transaction_date) ASC
  )                                                   AS rnk
FROM user_transactions
)

SELECT
  w1.yr
  ,w1.product_id
  ,w1.spend                                           AS curr_year_spend
  ,w2.spend                                           AS prev_year_spend
  ,ROUND((w1.spend - w2.spend) / w2.spend * 100, 2)   AS yoy_rate 
FROM window1  w1
LEFT OUTER JOIN window1  w2  
  ON w1.rnk = w2.rnk + 1
  AND w1.product_id = w2.product_id