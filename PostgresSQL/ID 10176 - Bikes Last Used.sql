/*

Question Id: ID 10176
Question: Bikes Last Used
URL: https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=1
Difficulty Level: Easy
Company Name: Lyft

*/

/* Solution */

SELECT DISTINCT bike_number,MAX(end_time) OVER (PARTITION BY bike_number) AS last_time_used
FROM dc_bikeshare_q1_2012
ORDER BY last_time_used DESC ;