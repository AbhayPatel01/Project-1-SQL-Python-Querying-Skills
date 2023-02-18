'''

Question Id: ID 10064
Question: Highest Energy Consumption
URL: https://platform.stratascratch.com/coding/10064-highest-energy-consumption?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

(
    pd.concat([fb_asia_energy,fb_eu_energy,fb_na_energy])
      .groupby('date',as_index=False)
      .sum()
      .pipe(lambda df: df[['consumption']]
                        .max()
                        .to_frame()
                        .rename(columns={0:'consumption'})
                        .merge(df,on='consumption',how='inner')
                        )
      [['date','consumption']]
     
    
)