/*

Question Id: ID 10159
Question: Ranking Most Active Guests
URL: https://platform.stratascratch.com/coding/10159-ranking-most-active-guests?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

*/

/* Solution */
WITH guest_num_messages AS 
    (SELECT id_guest, SUM(n_messages) AS total_message_sent
    FROM airbnb_contacts
    GROUP BY id_guest) 


SELECT DENSE_RANK() OVER(ORDER BY total_message_sent DESC) AS guest_rank, 
       id_guest,
        total_message_sent
FROM guest_num_messages;