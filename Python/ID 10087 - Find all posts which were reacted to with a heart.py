'''

Question Id: ID 10087
Question: Find all posts which were reacted to with a heart
URL: https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=1
Difficulty Level: Easy
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

(
    facebook_reactions
        .query("reaction == 'heart'")
        .merge(facebook_posts,
               on='post_id',
               how='inner')
        .iloc[:,4:]
        .rename(columns={'poster_y':'poster'})
        .drop_duplicates()
)