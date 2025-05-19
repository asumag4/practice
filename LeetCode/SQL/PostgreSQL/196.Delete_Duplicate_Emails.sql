-- Write your PostgreSQL query statement below

DELETE FROM Person 
-- JOIN Person p2 ON p2.email = Person.email AND p2.id > Person.id; -- MySQL Way
USING Person p2
WHERE p2.email = Person.email AND p2.id > Person.id 

-- **BEST SOLUTION** 

DELETE FROM Person p1 USING Person p2
WHERE p1.email = p2.email
  AND p1.id > p2.id;

-- ** Why the best solution is better
-- 1. Short hand names for tables 
-- 2. least number of lines as possible