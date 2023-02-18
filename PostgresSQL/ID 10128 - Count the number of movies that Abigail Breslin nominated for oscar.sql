/*

Question Id: ID 10128
Question: Count the number of movies that Abigail Breslin nominated for oscar
URL: https://platform.stratascratch.com/coding/10128-count-the-number-of-movies-that-abigail-breslin-nominated-for-oscar?code_type=1
Difficulty Level: Easy
Company Name: Netflix

*/

/* Solution */
SELECT COUNT(*) 
FROM oscar_nominees
WHERE nominee = 'Abigail Breslin'