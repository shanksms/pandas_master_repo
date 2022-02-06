import pandas as pd


battle_dates_series = pd.read_csv('revolutionary_war.csv', usecols=['Start Date'], squeeze=True,
                                  parse_dates=['Start Date'])
battle_dates_series = battle_dates_series.dropna()
battle_days_series = battle_dates_series.apply(lambda battle_date: battle_date.strftime('%A'))
print(battle_days_series.value_counts())
