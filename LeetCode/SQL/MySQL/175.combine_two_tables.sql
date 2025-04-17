-- My Solution: 

SELECT 
    Person.firstName,
    Person.lastName,
    Address.city, 
    Address.state 
    FROM Person 
    LEFT JOIN Address 
        ON Person.personID = Address.personID 

Top Solution: 

-- BEST SOLUTION 

select firstname, lastname, city, state
from Person P
left join Address A
on P.personId = A.personId
