'''

Question Id: ID 9897
Question: Highest Salary In Department
URL: https://platform.stratascratch.com/coding/9897-highest-salary-in-department?code_type=1
Difficulty Level: Medium
Company Name: Twitter

'''

# Solution 
import pandas as pd

(
    employee
        [['department','salary']]
        .groupby('department',as_index=False)
        .max()
        .merge(employee,on='salary',how='inner')
        [['department_x','first_name','salary']]
        .rename(columns={'department_x':'department'})
) 