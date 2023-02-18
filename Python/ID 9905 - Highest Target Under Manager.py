'''

Question Id: ID 9905
Question: Highest Target Under Manager
URL: https://platform.stratascratch.com/coding/9905-highest-target-under-manager?code_type=1
Difficulty Level: Medium
Company Name: Salesforce

'''

# Solution 
import pandas as pd

(
    salesforce_employees
        .query('manager_id == 13')
        .pipe(lambda df: df.query(f'target == {df.target.max()}'))
        [["first_name","target"]]
) 
