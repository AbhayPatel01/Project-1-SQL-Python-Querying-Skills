'''

Question Id: ID 10322
Question: Finding User Purchases
URL: https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=1
Difficulty Level: Medium
Company Name: Amazon

'''

# Solution 
import pandas as pd

(
    amazon_transactions
        .merge(amazon_transactions,on='user_id',how='inner')
        .pipe(lambda df: df.assign(day_diff = df.created_at_y.dt.day - df.created_at_x.dt.day))
        .query('id_x != id_y')
        .query('day_diff >= 0 & day_diff <= 7')
        .user_id
        .unique()
)