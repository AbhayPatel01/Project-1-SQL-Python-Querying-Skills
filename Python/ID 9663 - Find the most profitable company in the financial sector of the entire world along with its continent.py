'''

Question Id: ID 9663
Question: Find the most profitable company in the financial sector of the entire world along with its continent
URL: https://platform.stratascratch.com/coding/9663-find-the-most-profitable-company-in-the-financial-sector-of-the-entire-world-along-with-its-continent?code_type=1
Difficulty Level: Easy
Company Name: Forbes

'''

# Solution
import pandas as pd

(
    forbes_global_2010_2014
    .query("sector == 'Financials' & rank == 1")
    [['company','continent','sector','profits']]
) 
