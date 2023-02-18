/*

Question Id: ID 10046
Question: Top 5 States With 5 Star Businesses
URL: https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=1
Difficulty Level: Hard
Company Name: Yelp

*/

/* Solution */
SELECT state, five_star_businesses_count
FROM(
    SELECT *, DENSE_RANK() OVER (ORDER BY five_star_businesses_count DESC) AS state_rank
    FROM(
        SELECT state, COUNT(business_id) AS five_star_businesses_count  
        FROM yelp_business 
        WHERE stars = 5 
        GROUP BY state ) AS sub1 ) AS sub2 
WHERE state_rank < 5  
ORDER BY five_star_businesses_count DESC, state