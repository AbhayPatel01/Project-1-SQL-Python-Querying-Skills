/*

Question Id: ID 10319
Question: Monthly Percentage Difference
URL: https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=1
Difficulty Level: Hard
Company Name: Amazon

*/

/* Solution */
SELECT created_at, ROUND(CAST(percentage_change AS DECIMAL),2) AS percentage_change
FROM(SELECT created_at, ((curr_month_revenue - prev_month_revenue) / CAST(prev_month_revenue AS FLOAT)) * 100 AS percentage_change
FROM (SELECT created_at, revenue AS curr_month_revenue, LAG(revenue) OVER (ORDER BY created_at) AS prev_month_revenue
FROM
    (SELECT created_at, SUM(value) AS revenue
    FROM 
        (   SELECT SUBSTRING(CAST(created_at AS varchar),1,7) AS created_at, value
            FROM sf_transactions) AS sub1
    GROUP BY created_at) AS sub2) AS sub3) AS sub4