'''

Question Id: ID 10159
Question: Ranking Most Active Guests
URL: https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

'''

# Solution 
import pandas as pd

(
    airbnb_contacts
        [['id_guest','n_messages']]
        .groupby('id_guest')
        .sum()
        .reset_index()
        .pipe(lambda df: df.assign(rank=df.rank(numeric_only=True,method='dense',axis=0,ascending=False)))
        .sort_values(by='rank')
)
