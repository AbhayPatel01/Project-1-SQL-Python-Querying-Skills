'''

Question Id: ID 9992
Question: Find how many times each artist appeared on the Spotify ranking list
URL: https://platform.stratascratch.com/coding/9992-find-artists-that-have-been-on-spotify-the-most-number-of-times?code_type=1
Difficulty Level: Easy
Company Name: Spotify

'''

# Solution 
import pandas as pd

(
    spotify_worldwide_daily_song_ranking
        [['artist','id']]
        .groupby('artist',as_index=False)
        .count()
        .rename(columns={'id':'appearance_on_ranking_list'})
        .sort_values('appearance_on_ranking_list',ascending=False)
)