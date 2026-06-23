-- Most optimal solution

SELECT
  order_id,
  CASE
    WHEN order_id % 2 != 0 THEN LEAD(item, 1, item) OVER (ORDER BY order_id)
    ELSE LAG(item)                                   OVER (ORDER BY order_id)
  END AS item
FROM orders
ORDER BY order_id;