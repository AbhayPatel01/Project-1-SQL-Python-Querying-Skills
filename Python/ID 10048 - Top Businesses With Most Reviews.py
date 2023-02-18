'''

Question Id: ID 10048
Question: Top Businesses With Most Reviews
URL: https://platform.stratascratch.com/coding/10048-top-businesses-with-most-reviews?code_type=1
Difficulty Level: Medium
Company Name: Yelp

'''

# Solution 
import pandas as pd

(
    yelp_business
        [['name','review_count']]
            .sort_values('review_count',ascending=False)
            .head(5)
)