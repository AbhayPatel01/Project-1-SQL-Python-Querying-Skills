'''

Question Id: ID 9653
Question: Count the number of user events performed by MacBookPro users
URL: https://platform.stratascratch.com/coding/9653-count-the-number-of-user-events-performed-by-macbookpro-users?code_type=1
Difficulty Level: Easy
Company Name: Apple

'''

# Solution
import pandas as pd

(
    playbook_events
     
        .query("device == 'macbook pro'")
        [['event_name']]
        .value_counts()
        .reset_index()
)
