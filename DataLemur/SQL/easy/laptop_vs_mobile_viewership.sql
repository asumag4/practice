-- --- MY SOLUTION ---

SELECT 
  m.count AS mobile_views,
  l.count AS laptop_views
FROM 
-- Aggregate the each device type 
  (SELECT 
    COUNT(*) AS count
  FROM viewership
  WHERE device_type = 'tablet' OR device_type = 'phone'
  ) AS m,
  (SELECT 
    COUNT(*) AS count
  FROM viewership
  WHERE device_type = 'laptop'
  ) AS l;

-- --- BEST SOLUTION ---

SELECT 
  COUNT(*) FILTER (WHERE device_type = 'laptop') AS laptop_views,
  COUNT(*) FILTER (WHERE device_type IN ('tablet', 'phone'))  AS mobile_views 
FROM viewership;

-- Make use of the "FILTER" key word for "sub-query" like structures