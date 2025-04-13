# --- MY SOLUTION ---

import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(data=student_data, columns=["student_id", "age"])
    return df

print(createDataframe([[1,15],[2,11],[3,11],[4,20]]))

# --- BEST SOLUTION --- 

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    column_names = ["student_id", "age"]
    result_format = pd.DataFrame(student_data,columns=column_names)
    return result_format