/*

Question Id: ID 9992
Question: Find how many times each artist appeared on the Spotify ranking list
URL: https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=1
Difficulty Level: Easy
Company Name: Spotify

*/

/* Solution */
select artist, COUNT(position) AS number_of_occurences
FROM spotify_worldwide_daily_song_ranking
GROUP BY artist 
ORDER BY number_of_occurences DESC