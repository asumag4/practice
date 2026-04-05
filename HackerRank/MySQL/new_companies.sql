-- MY ANSWER

SELECT 
    c.company_code, 
    c.founder, 
    t1.lm_count,
    t2.sm_count,
    t3.m_count,
    t4.e_count
FROM Company c 
INNER JOIN( 
    SELECT 
        company_code,
        COUNT(DISTINCT lm.lead_manager_code) AS lm_count
    FROM Lead_Manager lm 
    GROUP BY company_code
    ) as t1 
    on c.company_code = t1.company_code
INNER JOIN (
    SELECT 
        company_code,
        COUNT(DISTINCT sm.senior_manager_code) AS sm_count
    FROM Senior_Manager sm
    GROUP BY company_code
    ) as t2 
    on c.company_code = t2.company_code 
INNER JOIN (
    SELECT 
        company_code,
        COUNT(DISTINCT m.manager_code) AS m_count
    FROM Manager m
    GROUP BY company_code
    ) as t3 
    on c.company_code = t3.company_code 
INNER JOIN (
    SELECT 
        company_code,
        COUNT(DISTINCT e.employee_code) AS e_count
    FROM Employee e
    GROUP BY company_code
    ) as t4
    on c.company_code = t4.company_code
ORDER BY c.company_code ASC;

-- BEST ANSWER 

select c.company_code, c.founder ,count(DISTINCT l.lead_manager_code),

count(DISTINCT s.senior_manager_code) ,count(DISTINCT m.manager_code),

count(DISTINCT e.employee_code)

from company c

join lead_manager l on c.company_code = l.company_code

join Senior_Manager s on l.lead_manager_code = s.lead_manager_code

join manager m on s.Senior_Manager_code = m.senior_manager_code

join employee e on m.manager_code = e.manager_code

group by c.company_code , c.founder

order by c.company_code;