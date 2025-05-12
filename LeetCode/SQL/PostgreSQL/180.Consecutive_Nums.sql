-- **MY SOLUTION**

SELECT 
    DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id + 1 AND l1.num = l2.num
JOIN Logs l3 ON l2.id = l3.id + 1 AND l2.num = l3.num

-- **BEST SOLUTION**

-- Write your PostgreSQL query statement below
SELECT distinct(num) AS ConsecutiveNums
FROM (SELECT num,LAG(num, 1) OVER (ORDER BY id) as prev1,
    LAG(num, 2) OVER (ORDER BY id) as prev2
        FROM Logs) AS subquery
WHERE num = prev1 AND num = prev2