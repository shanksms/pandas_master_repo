"""
Find contribution of each employee's towards daily sales
"""
import pandas as pd
sales_df = pd.read_csv("sales_by_employee.csv", parse_dates=['Date'])

daily_sales_by_emp = sales_df.pivot_table(
    index="Date",
    columns="Name",
    values="Revenue",
    aggfunc="sum"
)

print(daily_sales_by_emp)
daily_sales_by_emp = sales_df.pivot_table(
    index="Date",
    columns="Name",
    values="Revenue",
    aggfunc="sum",
    fill_value=0
)
print(daily_sales_by_emp)
# Add subtotal in each row
daily_sales_by_emp = sales_df.pivot_table(
    index="Date",
    columns="Name",
    values="Revenue",
    aggfunc="sum",
    fill_value=0,
    margins=True
)
print(daily_sales_by_emp)
# Lets pass a list of agg functions. It will create a multi index on columns
daily_sales_by_emp = sales_df.pivot_table(
    index="Date",
    columns="Name",
    values="Revenue",
    aggfunc=["sum", "count"],
    fill_value=0)
print(daily_sales_by_emp)

# Apply difference aggregation function on different columns
daily_sales_by_emp = sales_df.pivot_table(
    index="Date",
    columns="Name",
    values=["Revenue", 'Expenses'],
    aggfunc={'Revenue': 'min', 'Expenses': 'max'},
    fill_value=0)
print(daily_sales_by_emp)

# Stack multiple groupings on index axis
daily_sales_by_emp = sales_df.pivot_table(
    index=["Date", 'Name'],
    values=["Revenue", 'Expenses'],
    aggfunc='sum',
    fill_value=0)
print(daily_sales_by_emp)