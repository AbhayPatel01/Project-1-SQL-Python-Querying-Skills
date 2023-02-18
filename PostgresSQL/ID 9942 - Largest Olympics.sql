/*

Question Id: ID 9942
Question: Largest Olympics
URL: https://platform.stratascratch.com/coding/9942-largest-olympics?code_type=1
Difficulty Level: Medium
Company Name: ESPN

*/

/* Solution */
WITH athletes_olympic_games_unique 
AS(
    SELECT DISTINCT id, games
    FROM olympics_athletes_events)
    

SELECT games, COUNT(id) AS count_athlete
FROM athletes_olympic_games_unique
GROUP BY games
ORDER BY count_athlete DESC
LIMIT 1