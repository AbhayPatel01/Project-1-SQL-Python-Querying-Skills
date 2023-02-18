/*

Question Id: ID 9782
Question: Customer Revenue In March
URL: https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

*/

/* Solution */
SELECT cust_id, SUM(total_order_cost) AS total_revenue
FROM orders 
WHERE LEFT(order_date::varchar,7) = '2019-03'
GROUP BY cust_id
ORDER BY total_revenue DESC