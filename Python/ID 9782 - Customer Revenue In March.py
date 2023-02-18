'''

Question Id: ID 9782
Question: Customer Revenue In March
URL: https://platform.stratascratch.com/coding/9782-customer-revenue-in-march?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

'''

# Solution
import pandas as pd

(
    orders
        .assign(year_month = orders.order_date.apply(lambda col:str(col)[:7]))
        .query('year_month == "2019-03"')
        [['cust_id','total_order_cost']]
        .groupby('cust_id',as_index=False)
        .sum()
        .rename(columns={'total_order_cost':'total_revenue_per_customer'})
        .sort_values('total_revenue_per_customer',ascending=False)
        
) 
