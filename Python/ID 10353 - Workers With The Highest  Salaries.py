'''

Question Id: ID 10353
Question: Workers With The Highest  Salaries
URL: https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=1
Difficulty Level: Medium
Company Name: DoorDash

'''

# Solution 
import pandas as pd

(
    title.rename(columns={'worker_ref_id':'worker_id'})
          .merge(worker,how='inner',on='worker_id')   
          [['worker_title','salary']]
          .groupby('worker_title',as_index=False)
          .max()
          .sort_values(by='salary',ascending=False)
          .pipe(lambda df: df.query('salary == salary.max()'))
)