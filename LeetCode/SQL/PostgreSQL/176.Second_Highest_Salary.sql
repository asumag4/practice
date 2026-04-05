--- MY SOLUTION ---

SELECT (
    SELECT 
        DISTINCT salary
    FROM Employee
    ORDER BY salary DESC 
    LIMIT 1 OFFSET 1
) AS SecondHighestSalary

--- **BEST SOLUTION** ---


-- 1. Create a new table `sorted_salaries` that will have the second highest salary in the first row
with sorted_salaries as ( 
    select distinct salary
    from Employee as e
    order by e.salary desc
    offset 1
-- 2. From `sorted_salaries`; get the second highest salary
), second_salary as (
    select t.salary as SecondHighestSalary
    from sorted_salaries as t
    order by t.salary desc
    limit 1
-- 3. Get the number of DISTINCT `salary` COUNTS
), salary_count as (
    select count(*) as count
    from sorted_salaries
)
-- 4. When there is less than one (0) salaries found, return null 
select case when count < 1 then null
            else (select * from second_salary)
            end
from salary_count

/* 

Why the Second Query May Be More Efficient:

    Intermediate Results: By using CTEs, the query avoids recomputing sorted distinct salaries repeatedly. 
    This can save time when the query is used in larger operations or combined with other logic.

    Clearer Intent: The breakdown of steps in CTEs makes the query more readable and easier to maintain, 
    especially in complex scenarios.

    Edge Case Handling: The explicit handling of scenarios where fewer than two salaries exist adds robustness.

Why the First Query is Simpler but Could Be Slower:

    The single nested query in the first example does not store intermediate results, so the database engine has 
    to recompute everything each time it's run.

    It lacks explicit handling of scenarios with fewer distinct salaries, which could lead to unintended behavior 
    depending on the database system's implementation.

*/