/*

Question Id: ID 10299
Question: Finding Updated Records
URL: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=1
Difficulty Level: Easy
Company Name: Microsoft

*/

/* Solution */
SELECT id, first_name, last_name, department_id, salary
FROM
(SELECT *, DENSE_RANK() OVER (PARTITION BY id ORDER BY salary DESC) AS rnk  
FROM ms_employee_salary) AS sub1
WHERE rnk = 1 
ORDER BY id