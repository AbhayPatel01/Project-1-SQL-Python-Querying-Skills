'''

Question Id: ID 10077
Question: Income By Title and Gender
URL: https://platform.stratascratch.com/coding/10077-income-by-title-and-gender?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

'''

# Solution 
import pandas as pd

(
        sf_bonus
            .groupby('worker_ref_id',as_index=False)
            .sum()
            .rename(columns={'worker_ref_id':'id'})
            .merge(sf_employee, 
                   on='id',
                   how='inner')
            .pipe(lambda df: df.assign(total_compensation=df.salary + df.bonus))
            [['employee_title','sex','total_compensation']]
            .groupby(['employee_title','sex'],as_index=False)
            .mean()
            .rename(columns={'sex':'gender','total_compesnation':'average_total_compensation'})
        
)