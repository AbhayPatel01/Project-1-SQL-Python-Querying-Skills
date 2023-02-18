'''

Question Id: ID 10026
Question: Find all wineries which produce wines by possessing aromas of plum, cherry, rose, or hazelnut
URL: https://platform.stratascratch.com/coding/10026-find-all-wineries-which-produce-wines-by-possessing-aromas-of-plum-cherry-rose-or-hazelnut?code_type=1
Difficulty Level: Medium
Company Name: Wine Magazine

'''

# Solution 
import pandas as pd
import re 

punc_list = " ! # \$ % & ' \( \) \* \+ , - \. \/ : ; < = > \? @ \[ \] \^ _ ` { \| } ~ ".split( )
punc_list.append('"')
def process_text(text):
    for punc_char in punc_list : 
        text = re.sub(f"{punc_char}"," ",text.lower())
    processed_text = re.sub(r'\s+',' ',text)
    
    found_text = re.findall(r'\bplum\b|\bcherry\b|\brose\b|\bhazelnut\b',text)
    #return (text,found_text,len(found_text) != 0) 
        # Shows the found text of interest, the processsed_text, boolean value.  
    return len(found_text) != 0


( 
        winemag_p1
                .assign(description_contains_aroma_of_interest =   
                            winemag_p1
                                .description
                                .apply(process_text))
                .query('description_contains_aroma_of_interest == True')
                .winery
)