/*

Question Id: ID 9688
Question: Churro Activity Date
URL: https://platform.stratascratch.com/coding/9688-churro-activity-date?code_type=1
Difficulty Level: Easy
Company Name: City of Los Angeles

*/

/* Solution */
SELECT activity_date, pe_description 
FROM los_angeles_restaurant_health_inspections
WHERE facility_name = 'STREET CHURROS'
AND score < 95