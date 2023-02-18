'''

Question Id: ID 10299
Question: Finding Updated Records
URL: https://platform.stratascratch.com/coding/10299-finding-updated-records?code_type=1
Difficulty Level: Easy
Company Name: Microsoft

'''

# Solution 
import pandas as pd

(
        ms_employee_salary
            .groupby(['id','first_name','last_name','department_id'],as_index=False)
            .max()
            .sort_values(by='id')
        
)