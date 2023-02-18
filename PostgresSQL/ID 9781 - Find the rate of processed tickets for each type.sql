/*

Question Id: ID 9781
Question: Find the rate of processed tickets for each type
URL: https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

*/

/* Solution */
SELECT type, SUM(processed_int)/COUNT(type)::FLOAT AS rate_ticket_processed
FROM
(SELECT *, 
    CASE WHEN processed = TRUE THEN 1
         ELSE 0 
    END AS processed_int
FROM facebook_complaints) AS sub1
GROUP BY type