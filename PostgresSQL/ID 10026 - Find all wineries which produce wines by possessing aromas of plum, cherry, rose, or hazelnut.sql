/*

Question Id: ID 10026
Question: Find all wineries which produce wines by possessing aromas of plum, cherry, rose, or hazelnut
URL: https://platform.stratascratch.com/coding/10026-find-all-wineries-which-produce-wines-by-possessing-aromas-of-plum-cherry-rose-or-hazelnut?code_type=1
Difficulty Level: Medium
Company Name: Wine Magazine

*/

/* Solution */
WITH winerymag_processed AS (
SELECT winery, lower(description) as description 
FROM winemag_p1
) 

SELECT winery
FROM winerymag_processed 
WHERE description ~ '( |[-,."/])(cherry|rose|plum|hazelnut)( |[-,."/])'