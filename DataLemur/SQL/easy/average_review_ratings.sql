-- AVG(star rating)
-- GROUP BY product
-- GROUP BY month
SELECT
  EXTRACT('Month' FROM submit_date)   AS mth
  ,product_id
  ,ROUND(AVG(stars), 2)           AS avg_stars
FROM reviews
GROUP BY 
  mth
  ,product_id
ORDER BY 
  mth
  ,product_id