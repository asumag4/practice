SELECT
  ROUND(
  100.00 * COUNT(1) FILTER (WHERE call_category = 'n/a' OR call_category IS NULL)
  / COUNT(1)
  , 1)        AS uncategorised_call_pct
FROM callers