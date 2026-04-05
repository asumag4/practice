# --- MY SOLUTION ---

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    student_101 = students[students['student_id'] == 101]
    return student_101[['name','age']]

# --- BEST SOLUTION --- 

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]