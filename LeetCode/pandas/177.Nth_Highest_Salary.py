# --- MY SOLUTION ---

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    # Handling negative numbers 
    if N <= 0: 
        n_highest_sal = None
    else: 
        employee = employee.drop_duplicates(subset='salary').sort_values(by='salary', ascending=False)
        n_highest_sal = employee.iloc[N-1, 1] if len(employee) >= N else None 
    return pd.DataFrame({f"getNthHighestSalary({N})" : [n_highest_sal]})

# --- BEST SOLUTION ---

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    name = 'getNthHighestSalary(' + str(N) + ')'

    if employee['salary'].nunique() < N or N <= 0:
        return pd.DataFrame( {name: [None]} )
    val = employee['salary'].drop_duplicates().sort_values(ascending=False).iloc[N - 1]
    return pd.DataFrame( {name: [val]} )

# --- TEST CASES --- 

data = [[1,100],[2,200],[3,300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 2)) # 200

data = [[1,100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 2)) # None

# Same values for only two in the df
data = [[1, 100],[2,100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 2)) # None

# Same values for only two in the df
data = [[1, 100],[2,100]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 1)) # 100

# Same values for first two
data = [[1, 100],[2,100],[3,50]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 2)) # 50

# Same values for last two 
data = [[1, 100],[2,50],[3,50],[4,40]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, 3)) # 40

data = [[1,100],[2,200],[3,300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
print(nth_highest_salary(employee, -1)) # None