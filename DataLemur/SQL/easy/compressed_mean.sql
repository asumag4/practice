-- SELECT 
--   ROUND(mean::NUMERIC, 1) AS mean
-- FROM 
-- (
SELECT
  ROUND(
    SUM(item_count * order_occurrences)::NUMERIC / SUM(order_occurrences)::NUMERIC
    , 1
  ) AS mean
FROM items_per_order
-- ) t