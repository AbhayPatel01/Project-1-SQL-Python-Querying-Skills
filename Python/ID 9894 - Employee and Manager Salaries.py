'''

Question Id: ID 9894
Question: Employee and Manager Salaries
URL: https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=1
Difficulty Level: Medium
Company Name: Dropbox

'''

# Solution 
import pandas as pd

(
    employee 
        .merge(employee,left_on='manager_id',right_on='id')
        .query("salary_x > salary_y")
        [['first_name_x','salary_x']]
)
