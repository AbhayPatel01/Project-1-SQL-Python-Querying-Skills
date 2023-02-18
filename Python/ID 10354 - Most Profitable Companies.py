'''

Question Id: ID 10354
Question: Most Profitable Companies
URL: https://platform.stratascratch.com/coding/10354-most-profitable-companies?code_type=1
Difficulty Level: Medium
Company Name: Forbes

'''

# Solution 
import pandas as pd

(
    forbes_global_2010_2014
        [['company','profits']]
        .groupby('company',as_index=False)
        .sum()
        .sort_values(by='profits',ascending=False)
        .head(3)
)