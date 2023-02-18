/*

Question Id: ID 9726
Question: Classify Business Type
URL: https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=1
Difficulty Level: Medium
Company Name: City of San Francisco

*/

/* Solution */
SELECT DISTINCT business_name, 
      CASE 
        WHEN business_name ~ ' ?[rR][eE][sS][tT][aA][uU][rR][aA][nN][tT] ?' THEN 'restaurant'
        WHEN business_name ~ ' ?([cC][aA][fF][eE]|[Cc][aA][fF][éÉ]|[cC][oO][fF]{2}[eE]{2}) ?' THEN 'cafe'
        WHEN business_name ~ ' ?[sS][cC][hH][oO]{2}[lL] ?' THEN 'school' 
        ELSE 'other'
        END AS category 
FROM sf_restaurant_health_violations