/*

Question Id: ID 10322
Question: Finding User Purchases
URL: https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1
Difficulty Level: Medium
Company Name: Amazon

*/

/* Solution */
SELECT DISTINCT amz_trnsc1.user_id
FROM amazon_transactions AS amz_trnsc1
JOIN amazon_transactions AS amz_trnsc2 
ON amz_trnsc1.user_id = amz_trnsc2.user_id
AND amz_trnsc1.id != amz_trnsc2.id
AND DATEDIFF(amz_trnsc1.created_at,amz_trnsc2.created_at) BETWEEN -7 AND 7 
ORDER BY amz_trnsc1.user_id