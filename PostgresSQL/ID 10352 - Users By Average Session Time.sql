/*

Question Id: ID 10352
Question: Users By Average Session Time
URL: https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

*/

/* Solution */
WITH desired_facebook_web_log AS(
    SELECT user_id,action,timestamp::date As date, timestamp::time AS time
    FROM facebook_web_log
    WHERE action IN ('page_load','page_exit')
)


SELECT sub1.user_id, AVG(min_exit_time - max_load_time) AS avg_session_time_usage
FROM
    (SELECT DISTINCT user_id,date,MAX(time) OVER (PARTITION BY user_id,date) AS max_load_time
    FROM desired_facebook_web_log
    WHERE action = 'page_load') AS sub1 
INNER JOIN
    (SELECT DISTINCT user_id,date,MIN(time) OVER (PARTITION BY user_id,date) AS min_exit_time
    FROM desired_facebook_web_log
    WHERE action = 'page_exit') AS sub2 
ON sub1.user_id = sub2.user_id AND sub1.date = sub2.date
GROUP BY sub1.user_id