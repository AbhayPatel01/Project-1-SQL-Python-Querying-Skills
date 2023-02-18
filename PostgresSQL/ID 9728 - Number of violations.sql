/*

Question Id: ID 9728
Question: Number of violations
URL: https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

*/

/* Solution */
SELECT year, COUNT(violation_id)
FROM (SELECT  *, LEFT(inspection_date::varchar,4) AS year
FROM sf_restaurant_health_violations
WHERE business_name = 'Roxanne Cafe') AS sub1 
GROUP BY year 
ORDER BY year