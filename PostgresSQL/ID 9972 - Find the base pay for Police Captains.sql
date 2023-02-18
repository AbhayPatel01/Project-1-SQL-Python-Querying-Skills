/*

Question Id: ID 9972
Question: Find the base pay for Police Captains
URL: https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=1
Difficulty Level: Easy
Company Name: City of San Francisco

*/

/* Solution */
SELECT employeename, basepay 
FROM sf_public_salaries
WHERE lower(jobtitle) LIKE '%police%';