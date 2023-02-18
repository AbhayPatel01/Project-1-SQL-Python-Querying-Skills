/*

Question Id: ID 9891
Question: Customer Details
URL: https://platform.stratascratch.com/coding/9891-customer-details?code_type=1
Difficulty Level: Easy
Company Name: Amazon

*/

/* Solution */
SELECT first_name, last_name, city, order_details
FROM  customers
LEFT JOIN  orders 
ON orders.cust_id  = customers.id  
ORDER BY first_name, order_details