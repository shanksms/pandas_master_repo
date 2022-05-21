
"""
Find "favorite" customers based on the order count and the total cost of orders.
A customer is considered as a favorite if he or she has placed more than 3 orders and with
the total cost of orders more than $100.

Output the customer's first name, city, number of orders, and total cost of orders.
"""

import pandas as pd

customers = pd.read_csv('../data_files/customers.csv')
orders = pd.read_csv('../data_files/orders.csv')

customer_order_df = pd.merge(customers, orders, left_on='id', right_on='cust_id')
grouped_df = customer_order_df.groupby(
    ['id_x', 'first_name', 'city']
).agg(dict(id_y='count', total_order_cost='sum')).reset_index()

result = grouped_df.loc[(grouped_df['id_y']) > 3 & (grouped_df['total_order_cost'] > 300), :]
print(result)