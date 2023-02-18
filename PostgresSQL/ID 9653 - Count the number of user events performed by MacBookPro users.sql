/*

Question Id: ID 9653
Question: Count the number of user events performed by MacBookPro users
URL: https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=1
Difficulty Level: Easy
Company Name: Apple

*/

/* Solution */
SELECT event_name, COUNT(*) AS event_count
FROM playbook_events 
WHERE lower(device) = 'macbook pro' 
GROUP BY 1