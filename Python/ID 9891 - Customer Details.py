'''

Question Id: ID 9891
Question: Customer Details
URL: https://platform.stratascratch.com/coding/9891-customer-details?code_type=1
Difficulty Level: Easy
Company Name: Amazon

'''

# Solution 
import pandas as pd

(
    customers
        .rename(columns={'id':'cust_id'})
        .merge(orders,on='cust_id',how='left')
        [['first_name','last_name','city','order_details']]
        .sort_values(['first_name','order_details'])
    
) 
