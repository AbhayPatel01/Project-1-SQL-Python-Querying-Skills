/*

Question Id: ID 9632
Question: Host Popularity Rental Prices
URL: https://platform.stratascratch.com/coding/9632-host-popularity-rental-prices?code_type=1
Difficulty Level: Hard
Company Name: Airbnb

*/

/* Solution */
WITH airbnb_host_searches_processed AS (

    SELECT *, CASE WHEN number_of_reviews = 0 THEN 'New'
               WHEN number_of_reviews >= 1 AND number_of_reviews <= 5 THEN 'Rising'
               WHEN number_of_reviews >= 6 AND number_of_reviews <= 15 THEN 'Trending Up'
               WHEN number_of_reviews >= 16 AND number_of_reviews <= 40 THEN 'Popular'
               ELSE 'Hot'
             END AS popularity_rating,
        CONCAT(price,room_type,host_since,zipcode,number_of_reviews) AS host_id 
    FROM airbnb_host_searches
)
 
SELECT popularity_rating, 
       MIN(price) AS min_rental_price, 
       AVG(price) AS avg_rental_price,
       MAX(price) AS max_rental_price
FROM    
    (SELECT DISTINCT host_id,price,popularity_rating
    FROM airbnb_host_searches_processed) AS sub1 
GROUP BY popularity_rating