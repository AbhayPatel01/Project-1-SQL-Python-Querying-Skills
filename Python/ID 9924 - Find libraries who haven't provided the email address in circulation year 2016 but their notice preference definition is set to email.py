'''

Question Id: ID 9924
Question: Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email
URL: https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?code_type=1
Difficulty Level: Easy
Company Name: City of San Francisco

'''

# Solution 
import pandas as pd

(
    library_usage
        .query("notice_preference_definition == 'email' \
                & provided_email_address == False \
                & circulation_active_year == 2016 ")
        [['home_library_code']]
        .drop_duplicates()
)