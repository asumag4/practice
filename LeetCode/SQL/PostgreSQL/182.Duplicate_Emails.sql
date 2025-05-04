-- **LEARNED SOLUTION**

-- Grab the emails 
SELECT 
    email AS Email
FROM Person 
GROUP BY email
HAVING COUNT(Person.email) > 1 

-- You can aggregate the emails and going the number of occurances to count for duplicates, triplicates... etc.

-- **BEST SOLUTION** 

SELECT 
    email -- Just reference the variable 
GROUP BY email 
HAVING COUNT(*) > 1; -- Faster to count all rows than to select for one row at all