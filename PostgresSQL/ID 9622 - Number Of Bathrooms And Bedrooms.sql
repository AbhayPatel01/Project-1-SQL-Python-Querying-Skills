/*

Question Id: ID 9622
Question: Number Of Bathrooms And Bedrooms
URL: https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=1
Difficulty Level: Easy
Company Name: Airbnb

*/

/* Solution */
SELECT city, property_type, AVG(bathrooms) AS avg_bathrooms, AVG(bedrooms) AS avg_bedrooms
FROM airbnb_search_details
GROUP BY city, property_type