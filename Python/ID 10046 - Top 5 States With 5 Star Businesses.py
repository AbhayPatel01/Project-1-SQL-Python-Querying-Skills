'''

Question Id: ID 10046
Question: Top 5 States With 5 Star Businesses
URL: https://platform.stratascratch.com/coding/10046-top-5-states-with-5-star-businesses?code_type=1
Difficulty Level: Hard
Company Name: Yelp

'''

# Solution 
import pandas as pd

(
    yelp_business
        .query('stars == 5')
        [['state']]
        .value_counts()
        .reset_index()
        .rename(columns={0:'five_start_businesses_count'})
        .pipe(lambda df: 
                        df.assign(state_rank=df['five_start_businesses_count']
                                    .rank(method='dense',ascending=False)
                                )
            )
        .query('state_rank < 5')
        [['state','five_start_businesses_count']]
)