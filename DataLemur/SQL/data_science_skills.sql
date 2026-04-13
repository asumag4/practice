-- My Answer

SELECT
  candidate_id
FROM (
  SELECT
    *
  FROM candidates
  WHERE 
    skill IN (
    'Python'
    ,'Tableau'
    ,'PostgreSQL'
    ) 
  ) filtered
GROUP BY candidate_id
HAVING COUNT(candidate_id) >= 3

-- Best Answer 
SELECT 
    candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id;