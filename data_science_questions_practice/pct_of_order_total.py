import pandas as pd

"""
Transform function returns series having same shape as sub group. It duplicates the result of aggregation in each 
element of the series.
https://pbpython.com/pandas_transform.html
The question we would like to answer is: “What percentage of the order total does each sku represent?”

For example, if we look at order 10001 with a total of $576.12, the break down would be:

B1-20000 = $235.83 or 40.9%
S1-27722 = $232.32 or 40.3%
B1-86481 = $107.97 or 18.7%
"""

sales_df = pd.read_csv('data_files/sales_data.csv')

def using_transform():
    sales_df['pct_of_total_value'] = sales_df['ext price'] / sales_df.groupby('account')['ext price'].transform('sum')
    print(sales_df)


if __name__ == '__main__':
    using_transform()