import pandas as pd
"""
Write a query that'll identify returning active users. A returning active user is a user that has made a
second purchase within 7 days of any other of their purchases. Output a list of user_ids of these returning active 
users.
"""
user_transactions = pd.read_csv('data_files/user_purchase.csv')
user_transactions['created_at'] = pd.to_datetime(user_transactions['created_at']).dt.date
user_transactions = user_transactions.sort_values(by=['user_id', 'created_at'], ascending=[True, True])
user_transactions['prev_value'] = user_transactions.groupby('user_id')['created_at'].shift()
user_transactions['days_difference'] = (user_transactions['created_at'] - user_transactions['prev_value']).dt.days

print(user_transactions[user_transactions['days_difference'] <= 7]['user_id'])