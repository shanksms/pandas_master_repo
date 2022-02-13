import pandas as pd
"""
In  [97] citi_bike = pd.read_csv("citibike.csv")
         citi_bike.head()

Out [97]
                 start_time                 stop_time
0  2020-06-01 00:00:03.3720  2020-06-01 00:17:46.2080
1  2020-06-01 00:00:03.5530  2020-06-01 01:03:33.9360
2  2020-06-01 00:00:09.6140  2020-06-01 00:17:06.8330
3  2020-06-01 00:00:12.1780  2020-06-01 00:03:58.8640
4  2020-06-01 00:00:21.2550  2020-06-01 00:24:18.9650

Here are the challenges for this section:

Convert the start_time and stop_time columns to store datetime (Timestamp) values instead of strings.

Count the rides that occurred on each day of the week (Monday, Tuesday, and so on). Which weekday is the most popular for a bike ride? Use the start_time column as your starting point.

Count the rides per week for each week within the month. To do so, round each date in the start_time column to its previous or current Monday. Assume that each week starts on a Monday and ends on a Sunday. Thus, the first week of June would be Monday, June 1 through Sunday, June 7.

Calculate the duration of each ride, and save the results to a new duration column.

Find the average duration of a bike ride.

Extract the five longest bike rides by duration from the data set.
"""
city_bikes = pd.read_csv('citibike.csv')
print('#' * 80)
print(city_bikes.info())
city_bikes['start_time'] = pd.to_datetime(city_bikes['start_time'])
city_bikes['stop_time'] = pd.to_datetime(city_bikes['stop_time'])

print('#' * 80)
city_bikes.loc[:, 'day_name_of_week'] = city_bikes.loc[:, 'start_time'].dt.day_name()
print(city_bikes.loc[:, 'day_name_of_week'].value_counts())

print('#' * 80)

days_away_from_monday = city_bikes["start_time"].dt.dayofweek
dates_rounded_to_monday = city_bikes[
              "start_time"
          ] - pd.to_timedelta(days_away_from_monday, unit="day")
print(dates_rounded_to_monday.dt.date.value_counts())
print('#' * 80)
city_bikes["duration"] = (
        city_bikes["stop_time"] - city_bikes["start_time"]
)
print(city_bikes["duration"])
