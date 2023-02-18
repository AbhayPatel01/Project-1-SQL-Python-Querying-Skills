/*

Question Id: ID 10156
Question: Number Of Units Per Nationality
URL: https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

*/

/* Solution */
SELECT nationality, COUNT(DISTINCT unit_id)
FROM airbnb_hosts 
JOIN airbnb_units
ON airbnb_hosts.age < 30 AND airbnb_hosts.host_id = airbnb_units.host_id
    AND airbnb_units.unit_type = 'Apartment'
GROUP BY nationality