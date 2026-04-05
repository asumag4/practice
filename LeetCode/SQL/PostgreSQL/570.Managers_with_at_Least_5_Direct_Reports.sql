l-- Write your PostgreSQL query statement below

-- IN managerID, count the occurance of each managerID, find the managerID's with atleast 5  

-- Then match the found managerID's with the id, then give the name 
SELECT 
    Employee.name
FROM Employee
JOIN (
    SELECT 
        managerID
    FROM Employee
    GROUP BY managerID
    HAVING COUNT(managerID) >= 5
) AS t1 ON t1.managerID = Employee.id;

-- ** BEST SOLUTION ** 

-- Write your PostgreSQL query statement below
SELECT employee.name
FROM Employee
WHERE id IN (
    SELECT
        managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)