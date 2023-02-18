'''

Question Id: ID 9726
Question: Classify Business Type
URL: https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

'''

# Solution 
import pandas as pd

def business_categoriser(text): 
    text = text.lower()
    if 'restaurant' in text:
        return 'restaurant'
    elif ('cafe' in text) or ('coffee' in text) or ('café' in text):
        return 'cafe'
    elif ('school' in text): 
        return 'school'
    else:
        return 'other'

(
    sf_restaurant_health_violations.assign(
       business_category = sf_restaurant_health_violations
        .business_name
        .apply(business_categoriser))
        [['business_name','business_category']]
        .drop_duplicates()

) 
