-- My Answer 

SELECT 
  page_id
FROM pages
WHERE page_id NOT IN (
  SELECT 
    page_id
  FROM page_likes
)
ORDER BY page_id ASC;

-- Best Answer
SELECT page_id
FROM pages
EXCEPT
SELECT page_id
FROM page_likes;