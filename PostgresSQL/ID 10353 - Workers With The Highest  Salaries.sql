/*

Question Id: ID 10353
Question: Workers With The Highest  Salaries
URL: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1
Difficulty Level: Medium
Company Name: DoorDash

*/

/* Solution */
SELECT worker_title, salary
FROM worker
JOIN title 
ON worker.worker_id = title.worker_ref_id 
WHERE salary = 
(SELECT MAX(salary)
FROM worker)