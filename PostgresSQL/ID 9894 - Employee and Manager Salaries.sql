/*

Question Id: ID 9894
Question: Employee and Manager Salaries
URL: https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=1
Difficulty Level: Medium
Company Name: Dropbox

*/

/* Solution */
SELECT emp1.first_name, emp1.salary
FROM employee emp1
JOIN employee emp2 
ON emp1.manager_id = emp2.id
WHERE emp1.salary > emp2.salary