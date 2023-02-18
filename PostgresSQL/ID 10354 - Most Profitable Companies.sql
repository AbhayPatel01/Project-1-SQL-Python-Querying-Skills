/*

Question Id: ID 10354
Question: Most Profitable Companies
URL: https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=1
Difficulty Level: Medium
Company Name: Forbes

*/

/* Solution */
SELECT company, SUM(profits) as profits
FROM forbes_global_2010_2014
GROUP BY company
ORDER BY profits DESC 
LIMIT 3