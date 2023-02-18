/*

Question Id: ID 10061
Question: Popularity of Hack
URL: https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=1
Difficulty Level: Easy
Company Name: Meta/Facebook

*/

/* Solution */
SELECT location, AVG(popularity) AS avg_popularity_of_programming_language_named_hack
FROM facebook_employees
JOIN facebook_hack_survey
ON facebook_hack_survey.employee_id = facebook_employees.id 
GROUP BY location