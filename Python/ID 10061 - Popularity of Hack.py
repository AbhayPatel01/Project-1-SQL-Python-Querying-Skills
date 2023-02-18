'''

Question Id: ID 10061
Question: Popularity of Hack
URL: https://platform.stratascratch.com/coding/10061-popularity-of-hack?code_type=1
Difficulty Level: Easy
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

(
        facebook_employees
            .rename(columns={'id':'employee_id'})
            .merge(facebook_hack_survey, 
                    on='employee_id')
            [['location','popularity']]
            .groupby('location',as_index=False)
            .mean()
            .rename(columns={'popularity':'avg_popularity'})
        
)