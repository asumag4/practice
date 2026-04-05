-- ** Using a window function can work **

-- ** BEST SOLUTION **
select score
     , dense_rank() over (order by score desc) as rank
from Scores

-- ** MY SOLUTION ** 

SELECT 
    s1.score,
    (
    SELECT 
        COUNT(DISTINCT s2.score)
    FROM Scores s2
    WHERE s2.score >= s1.score
    ) AS rank 
FROM Scores s1
ORDER BY score DESC