/*

Question Id: ID 10078
Question: Find matching hosts and guests in a way that they are both of the same gender and nationality
URL: https://platform.stratascratch.com/coding/10078-find-matching-hosts-and-guests-in-a-way-that-they-are-both-of-the-same-gender-and-nationality?code_type=1
Difficulty Level: Medium
Company Name: Airbnb

*/

/* Solution */
SELECT DISTINCT host_id, guest_id 
FROM airbnb_hosts
JOIN airbnb_guests
ON airbnb_hosts.gender = airbnb_guests.gender 
AND airbnb_hosts.nationality = airbnb_guests.nationality