/*

Question Id: ID 10285
Question: Acceptance Rate By Date
URL: https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

*/

/* Solution */
SELECT sub1.date, COUNT(sub2.action)/CAST(COUNT(sub1.action) AS FLOAT)AS col
FROM
(SELECT *
FROM fb_friend_requests AS fb1
WHERE fb1.action = 'sent') AS sub1
LEFT JOIN
(SELECT *
FROM fb_friend_requests AS fb2
WHERE fb2.action = 'accepted') AS sub2 
ON sub1.user_id_sender = sub2.user_id_sender
AND sub1.user_id_receiver = sub2.user_id_receiver
GROUP BY sub1.date
ORDER BY sub1.date