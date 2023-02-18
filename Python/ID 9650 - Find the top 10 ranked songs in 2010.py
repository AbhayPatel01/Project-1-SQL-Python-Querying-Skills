'''

Question Id: ID 9650
Question: Find the top 10 ranked songs in 2010
URL: https://platform.stratascratch.com/coding/9650-find-the-top-10-ranked-songs-in-2010?code_type=1
Difficulty Level: Medium
Company Name: Spotify

'''

# Solution
import pandas as pd

(
    billboard_top_100_year_end
        .query("year == 2010 & year_rank.between(1,10)")
        [['year_rank','group_name','song_name']]
        .drop_duplicates()
        .sort_values('year_rank')
) 
