# --- MY SOLUTION ---

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Organize by salary 
    if len(employee) > 1:
        
        # Sort the df by salary descending
        employee.sort_values(by='salary', ascending=False, inplace=True)
        
        # Iterate through to find the second most salary 
        for row in range(len(employee)):
            if employee.iloc[row,1] < employee.iloc[row-1,1]:
                return pd.DataFrame(data=[employee.iloc[row,1]], columns=['SecondHighestSalary'])

    return pd.DataFrame(data=[None], columns=['SecondHighestSalary'])

# --- BEST SOLUTION ---
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salary = employee.drop_duplicates("salary").sort_values("salary", ascending=False) # Dropping duplicates
    second_highest_salary = salary.iloc[1]["salary"] if len(salary) >= 2 else None # Using one line if statement 
    return pd.DataFrame({"SecondHighestSalary": [second_highest_salary]}) # Using a straight dictionary for lower complexity

# --- TEST CASES --- 

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # 200 

data = [[1, 100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # None

# Same values for only two in the df
data = [[1, 100],[2,100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # None

# Same values for only 
data = [[1, 100],[2,100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # None

# Same values for first two
data = [[1, 100],[2,100],[3,50]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # None

# Same values for last two 
data = [[1, 100],[2,50],[3,50],[4,40]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(second_highest_salary(employee)) # None

