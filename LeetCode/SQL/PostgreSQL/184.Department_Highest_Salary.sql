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

-- ** SECOND EDITION **

-- WITH HighestSalaries AS (
--     SELECT 
--         departmentId,
--         MAX(Salary) AS Salary
--     FROM Employee e 
--     GROUP BY departmentId
-- )
-- SELECT 
--     d.name AS Department,
--     e1.name AS Employee,
--     e1.salary AS Salary
-- FROM Department d
-- JOIN HighestSalaries ON d.id = HighestSalaries.departmentId
-- JOIN Employee e1 ON e1.Salary = HighestSalaries.Salary 

-- ** THIRD EDITION **

SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON d.id = e.departmentId
WHERE Salary = (
    SELECT 
    MAX(salary)
    FROM Employee 
    WHERE departmentId = e.departmentId
)

-- ** BEST SOLUTION **

with ranking as (
    select
        e.name,
        e.salary,
        e.departmentId as depId,
        rank() over (partition by departmentId order by salary desc) as r
    from 
        employee as e
)
select
    dep.name as "Department",
    ra.name as "Employee",
    ra.salary as "Salary"
from
    ranking as ra
left join
    department as dep
on
    ra.depId = dep.id
where
    ra.r = 1