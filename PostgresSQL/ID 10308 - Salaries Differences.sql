/*

Question Id: ID 10308
Question: Salaries Differences
URL: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=1
Difficulty Level: Easy
Company Name: Dropbox

*/

/* Solution */
WITH max_salary_dept AS (
SELECT department_id,MAX(salary) as max_salary
FROM db_employee
WHERE department_id IN (1,4)
GROUP BY department_id 
)

SELECT MAX(max_salary) - MIN(max_salary) AS absolute_difference
FROM max_salary_dept