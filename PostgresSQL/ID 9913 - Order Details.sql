/*

Question Id: ID 9913
Question: Order Details
URL: https://platform.stratascratch.com/coding/9913-order-details?code_type=1
Difficulty Level: Easy
Company Name: Amazon

*/

/* Solution */
SELECT first_name, order_date, order_details, total_order_cost
FROM customers 
JOIN orders
ON customers.id = orders.cust_id 
AND first_name IN ('Jill','Eva') 
ORDER BY customers.id