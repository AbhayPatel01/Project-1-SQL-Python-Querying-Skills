'''

Question Id: ID 10049
Question: Reviews of Categories
URL: https://platform.stratascratch.com/coding/10049-reviews-of-categories?code_type=1
Difficulty Level: Medium
Company Name: Yelp

'''

# Solution 
import pandas as pd

(
    yelp_business
        .assign(business_categories=yelp_business.categories.apply(lambda col_name: col_name.split(';')))
        [['business_categories','review_count']]
        .explode('business_categories')
        .groupby('business_categories',as_index=False)
        .sum()
        .rename(columns={'reveiew_count':'total_review_count'})
        .sort_values('review_count',ascending=False)
)