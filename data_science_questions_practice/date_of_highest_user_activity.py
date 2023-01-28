"""
Tiktok want to find out what were the top two most active user days during an advertising campaign they ran in the first week of August 2022 (between the 1st to the 7th).


Identify the two days with the highest user activity during the advertising campaign.
They've also specified that user activity must be measured in terms of unique users.
Output the day, date, and number of users.

day_of_week	date_visited	n_users
Sunday	2022-08-07 00:00:00	5
Wednesday	2022-08-03 00:00:00	4
Friday	2022-08-05 00:00:00	4
Saturday	2022-08-06 00:00:00	4


"""
import pandas as pd
user_streaks = pd.read_csv('data_files/user_streaks.csv', parse_dates=['date_visited'])
between_first_seventh = (user_streaks['date_visited'] >= pd.Timestamp('2022-08-01')) &  (user_streaks['date_visited'] <= pd.Timestamp('2022-08-07'))
user_streaks = user_streaks[between_first_seventh]
user_streaks = user_streaks.groupby(['date_visited'])['user_id'].nunique().reset_index(name='n_users').sort_values(by=['n_users'], ascending=False)
user_streaks['day_of_week'] = user_streaks['date_visited'].dt.day_name()
user_streaks['rank'] = user_streaks['n_users'].rank(method='dense')
user_streaks = user_streaks.nlargest(2, 'rank', keep='all')
print(user_streaks[['day_of_week', 'date_visited', 'n_users']])