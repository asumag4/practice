-- common table expression (CTE); temporary result to query from
with cte as( 
-- get the counts of each customer, via GROUP BY and COUNT() 
select customer_number,count(order_number) as total_order 
from Orders group by customer_number 
) 
select customer_number 
from cte 
-- Use WHERE X = Y, but Y = the MAX() from total_order in 'cte'
where total_order=(select max(total_order) from cte)

