/*

Question Id: ID 10284
Question: Popularity Percentage
URL: https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=1
Difficulty Level: Hard
Company Name: Meta/Facebook

*/

/* Solution */
SELECT user1 AS user_id, (friend_count/CAST(total_user_on_platform AS FLOAT)) * 100 AS popularity_percentage
FROM
(SELECT user1, COUNT(*) AS friend_count, (
    SELECT COUNT(*)
    FROM facebook_friends
) AS total_user_on_platform
FROM 
(SELECT user1,user2
FROM facebook_friends 
UNION
SELECT user2,user1 
FROM facebook_friends) AS sub1
GROUP BY user1) AS sub2
ORDER BY user1