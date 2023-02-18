'''

Question Id: ID 514
Question: Marketing Campaign Success [Advanced]
URL: https://platform.stratascratch.com/coding/514-marketing-campaign-success-advanced?code_type=1
Difficulty Level: Hard
Company Name: Amazon

'''

# Solution 
import pandas as pd

 (
    marketing_campaign
    [['user_id','product_id','created_at']]
    .groupby(['user_id','product_id'],as_index=False)
    .min()
    .merge(
        marketing_campaign 
        [['user_id','created_at']]
        .groupby('user_id',as_index=False)
        .min(),
        on = 'user_id',
        how = 'inner')
    .query('created_at_x != created_at_y')
    [['user_id']]
    .drop_duplicates()
    .count()
)