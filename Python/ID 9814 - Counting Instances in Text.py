'''

Question Id: ID 9814
Question: Counting Instances in Text
URL: https://platform.stratascratch.com/coding/9814-counting-instances-in-text?code_type=1
Difficulty Level: Hard
Company Name: Google

'''

# Solution 
import pandas as pd

(
google_file_store['contents']
    .str
    .lower()
    .str
    .split()
    .explode()
    .value_counts()
    .reset_index()
    .rename(columns={'index':'word'})
    .query("word in ['bull','bear']")
)
