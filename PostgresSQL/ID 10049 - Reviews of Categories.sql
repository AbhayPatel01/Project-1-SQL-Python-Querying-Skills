/*

Question Id: ID 10049
Question: Reviews of Categories
URL: https://platform.stratascratch.com/coding/10049-reviews-of-categories?code_type=1
Difficulty Level: Medium
Company Name: Yelp

*/

/* Solution */
SELECT business_category, SUM(review_count) AS total_review_count
FROM 
(SELECT *, unnest(string_to_array(categories,';')) As business_category
FROM yelp_business) AS sub1 
GROUP BY  business_category
ORDER BY total_review_count DESC