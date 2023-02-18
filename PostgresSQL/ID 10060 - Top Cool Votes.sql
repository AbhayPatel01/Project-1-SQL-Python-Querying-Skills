/*

Question Id: ID 10060
Question: Top Cool Votes
URL: https://platform.stratascratch.com/coding/10060-top-cool-votes?code_type=1
Difficulty Level: Medium
Company Name: Yelp

*/

/* Solution */
SELECT business_name, review_text
FROM yelp_reviews
WHERE cool =
(SELECT MAX(cool)
FROM yelp_reviews)