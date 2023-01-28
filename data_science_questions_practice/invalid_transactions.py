import pandas as pd

boi_transactions = pd.read_csv('data_files/bank_transactions.csv', parse_dates=['time_stamp'])
boi_transactions['day_of_week'] = boi_transactions['time_stamp'].dt.day_name()
boi_transactions['date'] = boi_transactions['time_stamp'].dt.date
boi_transactions['hour'] = boi_transactions['time_stamp'].dt.hour

sat_sunday_boolean_mask = (boi_transactions['day_of_week'] == 'Saturday') | (boi_transactions['day_of_week'] == 'Sunday')
res1 = boi_transactions[sat_sunday_boolean_mask]
boi_transactions = boi_transactions[~sat_sunday_boolean_mask]
holiday_boolean_mask = (boi_transactions['date'] == pd.Timestamp('2022-12-25')) | (boi_transactions['date'] == pd.Timestamp('2022-12-26'))
res2 = boi_transactions[holiday_boolean_mask]
boi_transactions = boi_transactions[~holiday_boolean_mask]
res3 = boi_transactions[(boi_transactions['hour'] < 9) | (boi_transactions['hour'] >= 16)]
res = pd.concat([res1, res2, res3])
print(res)