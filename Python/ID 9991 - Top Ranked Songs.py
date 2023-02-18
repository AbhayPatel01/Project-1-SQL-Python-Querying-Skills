'''

Question Id: ID 9991
Question: Top Ranked Songs
URL: https://platform.stratascratch.com/coding/9991-top-ranked-songs?code_type=1
Difficulty Level: Medium
Company Name: Spotify

'''

# Solution 
import pandas as pd

(
    spotify_worldwide_daily_song_ranking
        .query('position == 1')
        [['trackname','position']]
        .groupby('trackname',as_index=False)
        .count()
        .rename(columns={'position':'number_of_times_track_topped_spotify_ranking'})
        .sort_values('number_of_times_track_topped_spotify_ranking',ascending=False)
    
)