'''

Question Id: ID 10003
Question: Lyft Driver Wages
URL: https://platform.stratascratch.com/coding/10003-lyft-driver-wages?code_type=1
Difficulty Level: Easy
Company Name: Lyft

'''

# Solution 
import pandas as pd

(
    lyft_drivers
        .query('yearly_salary <= 30000 | yearly_salary >= 70000')
