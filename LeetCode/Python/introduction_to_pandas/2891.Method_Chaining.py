import pandas as pd 

# --- MY SOLUTION --- 

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    more_than_100_kg = animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)
    return more_than_100_kg[['name']]

# --- BEST SOLUTION --- 
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals['weight']>100].sort_values(by='weight',ascending=False)[['name']]