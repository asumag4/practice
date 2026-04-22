-- Determine the second highest salary among all employees

SELECT
  DISTINCT 
    t.salary
FROM (
  SELECT
    employee_id
    ,name
    ,salary
    ,department_id
    ,manager_id
    ,ROW_NUMBER() OVER (
    ORDER BY salary DESC
    ) AS row_num
  FROM employee
) t
WHERE t.row_num = 2