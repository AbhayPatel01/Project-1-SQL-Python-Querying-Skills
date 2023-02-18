/*

Question Id: ID 10077
Question: Income By Title and Gender
URL: https://platform.stratascratch.com/coding/10077-income-by-title-and-gender?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

*/

/* Solution */
SELECT employee_title, sex AS gender, AVG(total_salary) AS avg_salary
FROM
(SELECT *, salary + bonus AS total_salary
FROM sf_employee
JOIN (
SELECT worker_ref_id, SUM(bonus) AS bonus
FROM sf_bonus
GROUP BY worker_ref_id) AS sub1
ON sub1.worker_ref_id = sf_employee.id)  AS sub2 
GROUP BY employee_title, sex