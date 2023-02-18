/*

Question Id: ID 9897
Question: Highest Salary In Department
URL: https://platform.stratascratch.com/coding/9897-highest-salary-in-department?code_type=1
Difficulty Level: Medium
Company Name: Twitter

*/

/* Solution */
SELECT department, first_name, salary
FROM(
    SELECT *, RANK() OVER (PARTITION BY department ORDER BY SALARY DESC) AS salary_rank 
    FROM employee 
    ) AS sub1 
WHERE salary_rank = 1