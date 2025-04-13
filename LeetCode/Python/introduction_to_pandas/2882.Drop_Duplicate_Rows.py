# --- MY SOLUTION ---

import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email',keep='first')

# --- BEST SOLUTION --- 
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset = ['email']) 

# NOTE: default keep = 'first' 