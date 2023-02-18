'''

Question Id: ID 10176
Question: Bikes Last Used
URL: https://platform.stratascratch.com/coding/10176-bikes-last-used?code_type=1
Difficulty Level: Easy
Company Name: Lyft

'''

# Solution 
import pandas as pd

(dc_bikeshare_q1_2012
    [['bike_number','end_time']]
    .groupby(['bike_number'])
    .max()
    .reset_index()
    .sort_values('end_time',ascending=False)
)
