'''

Question Id: ID 9942
Question: Largest Olympics
URL: https://platform.stratascratch.com/coding/9942-largest-olympics?code_type=1
Difficulty Level: Medium
Company Name: ESPN

'''

# Solution 
import pandas as pd

(
    olympics_athletes_events
        [['id','games']]
        .drop_duplicates()
        .groupby('games',as_index = False)
        .count()
        .sort_values(by='id',ascending=False)
        .head(1)
        .rename(columns={'games':'olympic games','id':'count'})
    )