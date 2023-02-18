'''

Question Id: ID 9917
Question: Average Salaries
URL: https://platform.stratascratch.com/coding/9917-average-salaries?code_type=1
Difficulty Level: Easy
Company Name: Salesforce

'''

# Solution 
import pandas as pd

(
        employee
         [['department','salary']]
         .groupby('department',as_index=False)
         .mean()
         .merge(employee,how='inner',on='department')
         [['department','first_name','salary_y','salary_x']]
         .rename(columns={'salary_y':'salary','salary_x':'avg_salary'})
 )