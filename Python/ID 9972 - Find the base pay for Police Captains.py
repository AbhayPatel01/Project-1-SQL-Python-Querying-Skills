'''

Question Id: ID 9972
Question: Find the base pay for Police Captains
URL: https://platform.stratascratch.com/coding/9972-find-the-base-pay-for-police-captains?code_type=1
Difficulty Level: Easy
Company Name: City of San Francisco

'''

# Solution 
import pandas as pd

(
    sf_public_salaries
        .assign(contains_word_of_interest = sf_public_salaries
                                            .jobtitle
                                            .str
                                            .lower()
                                            .str
                                            .contains('police')
            )
        .query('contains_word_of_interest == True')
        [['employeename','basepay']]
    
)
