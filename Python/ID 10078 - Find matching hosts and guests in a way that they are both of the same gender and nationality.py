'''

Question Id: ID 10078
Question: Find matching hosts and guests in a way that they are both of the same gender and nationality
URL: https://platform.stratascratch.com/coding/10078-find-matching-hosts-and-guests-in-a-way-that-they-are-both-of-the-same-gender-and-nationality?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

'''

# Solution 
import pandas as pd

(
    airbnb_guests
        .merge(airbnb_hosts,
               on=['gender','nationality'],
               how='inner')
        .drop_duplicates()
        [['host_id','guest_id']]
    
)