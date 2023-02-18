/*

Question Id: ID 10087
Question: Find all posts which were reacted to with a heart
URL: https://platform.stratascratch.com/coding/10087-find-all-posts-which-were-reacted-to-with-a-heart?code_type=1
Difficulty Level: Easy
Company Name: Meta/Facebook

*/

/* Solution */
SELECT DISTINCT fb_p.*
FROM facebook_reactions
JOIN facebook_posts AS fb_p
ON facebook_reactions.post_id = fb_p.post_id
AND facebook_reactions.reaction = 'heart'
