/*

Question Id: ID 10300
Question: Premium vs Freemium
URL: https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=1
Difficulty Level: Hard
Company Name: Microsoft

*/

/* Solution */
WITH ms_data AS (
    SELECT date, paying_customer, SUM(ms_download_facts.downloads) AS total_downloads
    FROM ms_user_dimension
    JOIN ms_acc_dimension
    ON ms_user_dimension.acc_id = ms_acc_dimension.acc_id
    JOIN ms_download_facts
    ON ms_download_facts.user_id = ms_user_dimension.user_id
    GROUP BY date, paying_customer
    ) 

SELECT md1.date as date, md1.total_downloads AS non_paying_customer_downloads, 
        md2.total_downloads AS paying_customer_downloads
FROM ms_data AS md1 
JOIN ms_data AS md2
ON md1.paying_customer = 'no'
AND md2.paying_customer = 'yes'
AND md1.date = md2.date 
AND md1.total_downloads > md2.total_downloads
ORDER BY date