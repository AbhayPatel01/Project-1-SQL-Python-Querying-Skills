/*

Question Id: ID 9905
Question: Highest Target Under Manager
URL: https://platform.stratascratch.com/coding/9905-highest-target-under-manager?code_type=1
Difficulty Level: Medium
Company Name: Salesforce

*/

/* Solution */
SELECT * 
FROM salesforce_employees
WHERE manager_id = 13 AND
target = (SELECT MAX(target)
FROM salesforce_employees
WHERE manager_id = 13 
GROUP BY manager_id)