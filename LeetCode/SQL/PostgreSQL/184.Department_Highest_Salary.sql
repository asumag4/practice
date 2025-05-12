-- Write your PostgreSQL query statement below

-- Edge Cases: will have to look at more than 1 of the maximum salary 

-- LEFT Join on Department

-- We need to make a way to find the MAX salary, we can use MAX() function 

-- ** FIRST EDITION **
-- SELECT 
--     d.name AS Department,
--     MAX(Salary) AS Salary
-- FROM Employee e
-- JOIN Department d ON e.departmentid = d.id   
-- GROUP BY Department

-- 1. Select for the highest salaries from each department. 

-- 2. Do a LEFT JOIN on names, to match employees and their department IDs 

WITH HighestSalaries AS (
    SELECT 
        departmentId,
        MAX(Salary) AS Salary
    FROM Employee e 
    GROUP BY departmentId
)
SELECT 
    d.name AS Department,
    e1.name AS Employee,
    e1.salary AS Salary
FROM Department d
JOIN HighestSalaries ON d.id = HighestSalaries.departmentId
JOIN Employee e1 ON e1.Salary = HighestSalaries.Salary 

-- For some reason, this code gives out doubles.