'''

Question Id: ID 9622
Question: Number Of Bathrooms And Bedrooms
URL: https://platform.stratascratch.com/coding/9622-number-of-bathrooms-and-bedrooms?code_type=1
Difficulty Level: Easy
Company Name: Airbnb

'''

# Solution
import pandas as pd

(
    airbnb_search_details
        [['city','property_type','bedrooms','bathrooms']]
        .groupby(['city','property_type'],as_index=False)
        .mean()
        .rename(columns={'bedrooms':'mean_bedrooms','bathrooms':'mean_bathrooms'})
) 
