#  --- MY SOLUTION --- 

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

# For the test case; I'll just be using the previous example 
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    df = pd.DataFrame(data=student_data, columns=["student_id", "age"])
    return df

df = createDataframe([[1,15],[2,11],[3,11],[4,20]])
print(getDataframeSize(df))

