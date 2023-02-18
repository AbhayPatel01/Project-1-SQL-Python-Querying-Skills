'''

Question Id: ID 10352
Question: Users By Average Session Time
URL: https://platform.stratascratch.com/coding/10352-users-by-avg-session-time?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

def func(df):
    globals()['df'] = df
    return df

(
    facebook_web_log 
        .assign(date=facebook_web_log.timestamp.apply(lambda col: str(col).split()[0]),
                time=facebook_web_log.timestamp.apply(lambda col: str(col).split()[1]))
        .pipe(func)
        .query('action == "page_exit"')
        .groupby(['date','user_id'],as_index=False)
        .min()
        .merge( df 
                .query('action == "page_load"')
                .groupby(['date','user_id'],as_index=False)
                .max(), on=['date','user_id'],how='inner')
        .pipe(func)
        .assign(time_diff = df.timestamp_x - df.timestamp_y)
        [['user_id','time_diff']]
        .groupby('user_id')
        .agg([sum,len])
        .reset_index()
        .pipe(func)
        .assign(avg_time = df.iloc[:,1] / df.iloc[:,2] )
        [['user_id','avg_time']]
)