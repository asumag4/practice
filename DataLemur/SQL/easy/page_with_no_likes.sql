-- Return 0 liked pages 

SELECT
  page_id
FROM pages
EXCEPT
SELECT
  DISTINCT
    page_id
FROM page_likes
ORDER BY page_id