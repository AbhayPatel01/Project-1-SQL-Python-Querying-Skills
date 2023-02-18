/*

Question Id: ID 10064
Question: Highest Energy Consumption
URL: https://platform.stratascratch.com/coding/10064-highest-energy-consumption?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

*/

/* Solution */
SELECT date, total_energy_consumption
FROM
(SELECT date, total_energy_consumption ,RANK() OVER (ORDER BY total_energy_consumption DESC) AS rnk
FROM
(SELECT date, SUM(consumption) AS total_energy_consumption
FROM
(SELECT * FROM fb_eu_energy
UNION
SELECT * FROM fb_asia_energy
UNION 
SELECT * FROM fb_na_energy) AS sub1 
GROUP BY date) AS sub2) AS sub3
WHERE rnk = 1