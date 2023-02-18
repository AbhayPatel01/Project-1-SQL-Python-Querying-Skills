/*

Question Id: ID 514
Question: Marketing Campaign Success [Advanced]
URL: https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced?code_type=1
Difficulty Level: Hard
Company Name: Amazon

*/

/* Solution */
WITH condition1 AS(
SELECT user_id
FROM marketing_campaign 
GROUP BY user_id 
HAVING COUNT(DISTINCT created_at) > 1)


SELECT COUNT(DISTINCT sub3.user_id) AS marketing_campaign_success_user_count
FROM(
SELECT *
FROM
(SELECT marketing_campaign.*, RANK() OVER (PARTITION BY condition1.user_id ORDER BY created_at) AS rnk 
FROM marketing_campaign 
JOIN condition1 
ON condition1.user_id = marketing_campaign.user_id) AS sub1 
WHERE rnk != 1 ) AS sub3
LEFT JOIN 
(SELECT *
FROM
(SELECT marketing_campaign.*, RANK() OVER (PARTITION BY condition1.user_id ORDER BY created_at) AS rnk 
FROM marketing_campaign 
JOIN condition1 
ON condition1.user_id = marketing_campaign.user_id) AS sub2 
WHERE rnk = 1) AS sub4 
ON sub3.user_id = sub4.user_id AND sub3.product_id = sub4.product_id
WHERE sub4.user_id IS NULL
