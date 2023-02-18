'''

Question Id: ID 10300
Question: Premium vs Freemium
URL: https://platform.stratascratch.com/coding/10300-premium-vs-freemium?code_type=1
Difficulty Level: Hard
Company Name: Microsoft

'''

# Solution 
import pandas as pd

(   
    ms_user_dimension
    .merge(ms_acc_dimension,how='inner', on='acc_id')
    .merge(ms_download_facts, how='inner',on='user_id')
    .pivot_table(index='date',columns='paying_customer',values='downloads',aggfunc=sum)
    .reset_index()
    .query('no > yes')
  
)