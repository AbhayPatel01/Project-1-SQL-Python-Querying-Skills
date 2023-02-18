'''

Question Id: ID 10285
Question: Acceptance Rate By Date
URL: https://platform.stratascratch.com/coding/10285-acceptance-rate-by-date?code_type=1
Difficulty Level: Medium
Company Name: Meta/Facebook

'''

# Solution 
import pandas as pd

(
    fb_friend_requests
        .assign(record_request_id = fb_friend_requests.user_id_sender + fb_friend_requests.user_id_receiver)
        .query('action == "sent"')
        .merge(
            fb_friend_requests
            .assign(record_request_id = fb_friend_requests.user_id_sender + fb_friend_requests.user_id_receiver)
                .query('action == "accepted"'), how='left',on='record_request_id'
            )
        .groupby('date_x',as_index=False)
        [['action_x','action_y']]
        .count()
        .pipe(lambda df: df.assign(acceptance_rate = df.action_y/df.action_x))
        [['date_x','acceptance_rate']]
        .rename(columns={'date_x':'date'})
    
)
