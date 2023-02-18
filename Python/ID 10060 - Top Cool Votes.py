'''

Question Id: ID 10060
Question: Top Cool Votes
URL: https://platform.stratascratch.com/coding/10060-top-cool-votes?code_type=1
Difficulty Level: Medium
Company Name: Yelp

'''

# Solution 
import pandas as pd

(
    
    yelp_reviews
        .query(f"cool == {yelp_reviews['cool'].max()}")
        [['business_name','review_text','cool']]
)