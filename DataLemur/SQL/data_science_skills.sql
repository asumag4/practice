-- My Answer

SELECT 
  t.candidate_id
FROM (
-- Fix this sub-table
  SELECT 
    candidate_id, 
    string_agg(skill, ', ') AS skill
  FROM candidates
  WHERE skill IN ('Python','Tableau','PostgreSQL')
  GROUP BY candidate_id
) AS t
WHERE t.skill LIKE '%Python, Tableau, PostgreSQL%';
-- https://stackoverflow.com/questions/43870/how-to-concatenate-strings-of-a-string-field-in-a-postgresql-group-by-query

-- Best Answer 
SELECT 
    candidate_id
FROM candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY candidate_id
HAVING COUNT(skill) = 3
ORDER BY candidate_id;