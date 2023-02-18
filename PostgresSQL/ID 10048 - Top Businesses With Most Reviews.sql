/*

Question Id: ID 10048
Question: Top Businesses With Most Reviews
URL: https://platform.stratascratch.com/coding/10048-top-businesses-with-most-reviews?code_type=1
Difficulty Level: Medium
Company Name: Yelp

*/

/* Solution */
SELECT name, review_count 
FROM yelp_business
ORDER BY review_count DESC
LIMIT 5