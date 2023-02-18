'''

Question Id: ID 9632
Question: Host Popularity Rental Prices
URL: https://platform.stratascratch.com/coding/9632-host-popularity-rental-prices?code_type=1
Difficulty Level: Hard
Company Name: Airbnb

'''

# Solution
import pandas as pd

def to_rating(val):
    if val == 0: 
        return 'New' 
    elif val <= 5:
        return 'Rising'
    elif val <= 15: 
        return 'Trending Up' 
    elif val <= 40: 
        return 'Popular' 
    else: 
        return 'Hot'

avg = lambda col: col.mean()

(
    airbnb_host_searches
        .assign(popularity_rating=
                airbnb_host_searches
                .number_of_reviews
                .apply(to_rating))
                .iloc[:,1:]        
                .drop_duplicates()
                [['popularity_rating','price']]
                .groupby('popularity_rating',as_index=False)
                .agg(['min','max','mean'])
                .reset_index()
)
