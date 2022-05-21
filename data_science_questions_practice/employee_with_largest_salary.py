import pandas as pd
"""
Find the employee with the highest salary per department.
Output the department name, employee's first name along with the corresponding salary.
"""
# Start writing code
employee = pd.read_csv('data_files/employee.csv')

result_df = employee.groupby('department').apply(lambda df: df.nlargest(1, 'salary', keep='last')).reset_index(drop=True)

print(result_df.loc[:, ['department', 'first_name', 'salary']])