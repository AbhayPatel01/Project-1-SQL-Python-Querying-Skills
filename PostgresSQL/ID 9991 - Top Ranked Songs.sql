/*

Question Id: ID 9991
Question: Top Ranked Songs
URL: https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=1
Difficulty Level: Medium
Company Name: Spotify

*/

/* Solution */
SELECT trackname, COUNT(trackname) AS num_of_times_at_rank_1
FROM spotify_worldwide_daily_song_ranking
WHERE position = 1 
GROUP BY trackname
ORDER BY num_of_times_at_rank_1 DESC