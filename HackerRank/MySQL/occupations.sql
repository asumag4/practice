SELECT 
	MAX(CASE WHEN Occupation = 'Doctor' THEN Name ELSE NULL END) AS Doctor,
	MAX(CASE WHEN Occupation = 'Professor' THEN Name ELSE NULL END) AS Professor,
	MAX(CASE WHEN Occupation = 'Singer' THEN Name ELSE NULL END) AS Singer,
	MAX(CASE WHEN Occupation = 'Actor' THEN Name ELSE NULL END) AS Actor
FROM (
	SELECT
	-- 1. Select the name 
		Name, 
	-- 2. Select the occupation
		Occupation, 
	-- 3. Select the `row_number()` 
		row_number() OVER (PARTITION BY Occupation ORDER BY Name) AS rn 
	FROM OCCUPATIONS
) 
AS x GROUP BY rn;