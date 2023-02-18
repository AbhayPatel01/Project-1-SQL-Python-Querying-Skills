'''

Question Id: ID 10319
Question: Monthly Percentage Difference
URL: https://platform.stratascratch.com/coding/10319-monthly-percentage-difference?code_type=1
Difficulty Level: Hard
Company Name: Amazon

'''

# Solution 
import pandas as pd

pd.concat([
(
    sf_transactions
        .assign(year_month = sf_transactions.created_at.apply(lambda x: str(x).split()[0][:-3]),
                number = sf_transactions.created_at.apply(lambda x: int(str(x).split()[0][5:7])))
        [['year_month','value','number']]
        .groupby(['year_month','number'],as_index=False)
        .sum()
        .merge(
    right = sf_transactions
        .assign(year_month = sf_transactions.created_at.apply(lambda x: str(x).split()[0][:-3]),
                number = sf_transactions.created_at.apply(lambda x: int(str(x).split()[0][5:7]) + 1))
        [['year_month','value','number']]
        .groupby(['year_month','number'],as_index=False)
        .sum(),
    on = 'number',
    how = 'inner')
    .pipe(lambda df: df.assign(percentage=round((df.value_x - df.value_y)/df.value_y * 100,2))) 
    [['year_month_x','percentage']]
 ), pd.DataFrame([['2019-01','']],columns=['year_month_x','percentage'])]).sort_values('year_month_x')
