'''

Question Id: ID 9688
Question: Churro Activity Date
URL: https://platform.stratascratch.com/coding/9688-churro-activity-date?code_type=1
Difficulty Level: Easy
Company Name: City of Los Angeles

'''

# Solution
import pandas as pd

(
    los_angeles_restaurant_health_inspections
        .assign(date=los_angeles_restaurant_health_inspections.activity_date.dt.date)
        .query('facility_name == "STREET CHURROS" & score < 95')
        [['date','pe_description']]
)
