/*

Question Id: ID 9915
Question: Highest Cost Orders
URL: https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1
Difficulty Level: Medium
Company Name: Amazon

*/

/* Solution */
WITH processed_orders AS (
SELECT cust_id, order_date,SUM(total_order_cost) AS total_order_cost
FROM orders
GROUP BY cust_id, order_date
) 

SELECT first_name, total_order_cost, order_date
FROM customers 
JOIN processed_orders 
ON customers.id = processed_orders.cust_id
AND processed_orders.order_date BETWEEN  '2019-02-01' AND '2019-05-01'
ORDER BY total_order_cost DESC
LIMIT 1