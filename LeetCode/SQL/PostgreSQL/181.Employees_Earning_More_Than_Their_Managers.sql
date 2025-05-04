-- ** BEST SOLUTION **

-- Write your PostgreSQL query statement below
SELECT e1.name AS Employee
FROM Employee e1 JOIN Employee e2 ON e1.managerId = e2.id AND e1.salary > e2.salary -- Faster to do an `AND` statement than a `WHERE`


-- ** MY SOLUTION **
-- Write your PostgreSQL query statement below

SELECT 
    e.name AS Employee -- 3. Get the names as outputs as Employee
FROM employee e
JOIN employee m ON m.id = e.managerId -- 1. Match the employees to their managers
WHERE e.salary > m.salary; -- 2. Find where the employees are making more than their managers 
