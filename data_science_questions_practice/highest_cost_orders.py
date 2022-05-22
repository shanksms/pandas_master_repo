import pandas as pd

"""
Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. If customer had more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total cost of their items, and the date.
For simplicity, you can assume that every first name in the dataset is unique.
"""
customers_df = pd.read_csv('data_files/highest_cost_order_customers.csv')
orders_df = pd.read_csv('data_files/highest_cost_order_orders.csv')

def approach_1():
    """
    1. Join datasets of orders and customers
    2. group by joined dataframe with grouping keys: first_name and order date. sum daily order cost for each group
    3. Find out the record with maximum daily total order cost
    :return:
    """
    customer_orders_df = pd.merge(customers_df, orders_df, left_on='id', right_on='cust_id')

    grouped_df = customer_orders_df.groupby(['first_name', 'order_date']).agg({'total_order_cost': 'sum'}).reset_index()
    result_df = grouped_df[grouped_df['total_order_cost'] == grouped_df['total_order_cost'].max()].rename(
        columns={'total_order_cost': 'max_cost'})
    result_df['order_date'] = pd.to_datetime(result_df['order_date']).dt.date
    return result_df

if __name__ == '__main__':
    print(approach_1())