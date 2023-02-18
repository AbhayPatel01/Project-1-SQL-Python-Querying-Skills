'''

Question Id: ID 10284
Question: Popularity Percentage
URL: https://platform.stratascratch.com/coding/10284-popularity-percentage?code_type=1
Difficulty Level: Hard
Company Name: Meta/Facebook

'''

# Solution
import pandas as pd

(
    pd 
     .concat([facebook_friends[['user1']].rename(columns={'user1':'users'}),
             facebook_friends[['user2']].rename(columns={'user2':'users'})])
     .assign(counter=1)
     .groupby(by=['users'],as_index=False)
     .sum()
     .pipe(lambda df: pd.DataFrame([df.users,df.counter/ len(df.users) * 100]))
     .T
)
