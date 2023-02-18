/*

Question Id: ID 9924
Question: Find libraries who haven't provided the email address in circulation year 2016 but their notice preference definition is set to email
URL: https://platform.stratascratch.com/coding/9924-find-libraries-who-havent-provided-the-email-address-in-2016-but-their-notice-preference-definition-is-set-to-email?code_type=1
Difficulty Level: Easy
Company Name: City of San Francisco

*/

/* Solution */
SELECT DISTINCT home_library_code
FROM library_usage
WHERE circulation_active_year = 2016 
AND lower(notice_preference_definition) = 'email'
AND provided_email_address = FALSE