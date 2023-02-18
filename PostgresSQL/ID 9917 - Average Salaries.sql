/*

Question Id: ID 9917
Question: Average Salaries
URL: https://platform.stratascratch.com/coding/9917-average-salaries?code_type=1
Difficulty Level: Easy
Company Name: Salesforce

*/

/* Solution */
SELECT department, first_name, salary, AVG(salary) OVER (PARTITION BY department) AS avg_dept_salary
FROM employee;