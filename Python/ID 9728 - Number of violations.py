'''

Question Id: ID 9728
Question: Number of violations
URL: https://platform.stratascratch.com/coding/9728-inspections-that-resulted-in-violations?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

'''

# Solution 
import pandas as pd

(
    sf_restaurant_health_violations
        .assign(year=sf_restaurant_health_violations.inspection_date.dt.year)
        .query("business_name == 'Roxanne Cafe'")
        [['year','violation_id']]
        .groupby('year',as_index=False)
        .count()
        .rename(columns={'violation_id':'roxanne_cafe_health_inspection_violation_counts'})
        .sort_values('roxanne_cafe_health_inspection_violation_counts')

) 