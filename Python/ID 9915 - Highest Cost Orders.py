'''

Question Id: ID 9915
Question: Highest Cost Orders
URL: https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=1
Difficulty Level: Medium
Company Name: Amazon

'''

# Solution 
import pandas as pd

(
    orders
        [['cust_id','order_date','total_order_cost']]
        .groupby(['cust_id','order_date'],as_index=False)
        .sum()
        .rename(columns={'cust_id':'id','id':'order_id'})
        .merge(customers, on='id',how='inner')
        .assign(order_date_copy = orders.order_date)
        .set_index('order_date_copy')
        .loc['2019-02-01 00:00:00':'2019-05-01 00:00:00']
        .pipe(lambda df: df.query(f"total_order_cost == {df.total_order_cost.max()}"))
        [['first_name','total_order_cost','order_date']]
        .pipe(lambda df: df.assign(order_date_actual=df.order_date.apply(lambda x: x.date())))
        [['first_name','total_order_cost','order_date_actual']]
) 
