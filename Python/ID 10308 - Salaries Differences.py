'''

Question Id: ID 10308
Question: Salaries Differences
URL: https://platform.stratascratch.com/coding/10308-salaries-differences?code_type=1
Difficulty Level: Easy
Company Name: Dropbox

'''

# Solution 
import pandas as pd

abs_diff = lambda df: df.max() - df.min() 
(
    db_employee
        .query("department_id == 1 | department_id == 4")
        .groupby(['department_id'])
        .max()
        [['salary']]
        .pipe(abs_diff)
        .to_frame()
        .rename(columns={0:'abs_diff'})
)
