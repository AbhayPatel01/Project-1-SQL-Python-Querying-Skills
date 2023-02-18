'''

Question Id: ID 10156
Question: Number Of Units Per Nationality
URL: https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

'''

# Solution 
import pandas as pd

(
        airbnb_units
        .query('unit_type == "Apartment"')
        .merge(
            airbnb_hosts
                .query('age < 30')
            , on='host_id',how='inner'
            )
        [['nationality','unit_id']]
        .groupby('nationality',as_index=False)
        .nunique()
        .sort_values('unit_id',ascending=False)
)