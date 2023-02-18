/*

Question Id: ID 10003
Question: Lyft Driver Wages
URL: https://platform.stratascratch.com/coding/10003-lyft-driver-wages?code_type=1
Difficulty Level: Easy
Company Name: Lyft

*/

/* Solution */
SELECT * 
FROM lyft_drivers 
WHERE yearly_salary <= 30000 
 OR yearly_salary >= 70000