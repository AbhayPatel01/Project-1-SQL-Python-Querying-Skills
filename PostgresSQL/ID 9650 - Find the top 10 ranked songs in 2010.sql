/*

Question Id: ID 9650
Question: Find the top 10 ranked songs in 2010
URL: https://platform.stratascratch.com/coding/9650-find-the-top-10-ranked-songs-in-2010?code_type=1
Difficulty Level: Medium
Company Name: Spotify

*/

/* Solution */
SELECT DISTINCT year_rank, group_name, song_name
FROM billboard_top_100_year_end
WHERE year = 2010
AND year_rank BETWEEN 1 AND 10
ORDER BY year_rank