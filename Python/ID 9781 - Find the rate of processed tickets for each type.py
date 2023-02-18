'''

Question Id: ID 9781
Question: Find the rate of processed tickets for each type
URL: https://platform.stratascratch.com/coding/9781-find-the-rate-of-processed-tickets-for-each-type?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

(
    facebook_complaints
        .assign(processed_int = facebook_complaints.processed.apply(lambda col_name: 1 if col_name else 0) )
        [['type','processed_int']]
        .groupby('type')
        .agg([sum,len])
        .reset_index()
        .pipe(lambda df:  df.assign(rate=df.iloc[:,1]/df.iloc[:,2]))
        [['type','rate']]
) 
