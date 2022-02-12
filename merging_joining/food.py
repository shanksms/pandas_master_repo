
import pandas as pd

"""
Here are the challenges:

Concatenate the two weeks of sales data into one DataFrame. Assign the week1 DataFrame a key of "Week 1" and the week2 DataFrame a key of "Week 2".

Find the customers who ate at the restaurant both weeks.

Find the customers who ate at the restaurant both weeks and ordered the same item each week.

HINT You can join data sets on multiple columns by passing the on parameter a list of columns.

Identify which customers came in only on Week 1 and only on Week 2.

Each row in the week1 DataFrame identifies a customer who purchased a food item. For each row, pull in the customer’s information from the customers DataFrame.
"""

week1 = pd.read_csv("week_1_sales.csv")
week2 = pd.read_csv("week_2_sales.csv")
print(pd.concat(objs = [week1, week2], keys = ["Week 1", "Week 2"]))
print(pd.merge(left=week1, right=week2, on='Customer ID', how='inner').drop_duplicates(subset=['Customer ID']))
print(pd.merge(left=week1, right=week2, on=['Customer ID', 'Food ID'], how='inner').drop_duplicates(subset=['Customer ID']))
print(pd.merge(left=week1, right=week2, on=['Customer ID', 'Food ID'], how='outer', indicator=True))


