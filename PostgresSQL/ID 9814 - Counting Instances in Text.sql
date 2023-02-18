/*

Question Id: ID 9814
Question: Counting Instances in Text
URL: https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=1
Difficulty Level: Hard
Company Name: Google

*/

/* Solution */
SELECT 'bear' AS word_of_interest,SUM((length(contents) - length(REPLACE(contents,'bear',''))) / length('bear')) AS word_occurence
FROM google_file_store 
UNION
SELECT 'bull',SUM((length(contents) - length(REPLACE(contents,'bull',''))) / length('bull'))
FROM google_file_store 
