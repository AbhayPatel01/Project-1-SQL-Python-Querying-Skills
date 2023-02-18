'''

Question Id: ID 9913
Question: Order Details
URL: https://platform.stratascratch.com/coding/9913-order-details?code_type=1
Difficulty Level: Easy
Company Name: Amazon

'''

# Solution 
import pandas as pd

(
    customers
        .query('first_name in ["Jill","Eva"]')
        .rename(columns={'id':'cust_id'})
        .merge(orders,on='cust_id',how='inner')
        .sort_values('cust_id')
        [['first_name','order_date','order_details','total_order_cost']]
        
) 
