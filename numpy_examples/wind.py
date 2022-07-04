"""
https://github.com/enthought/Numpy-Tutorial-SciPyConf-2019/tree/master/exercises/wind_statistics

Wind Statistics
----------------
Topics: Using array methods over different axes, fancy indexing.
1. The data in 'wind.data' has the following format::
        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71
   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.
   Use the 'loadtxt' function from numpy to read the data into
   an array.
2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).
3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)
4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)
5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).
6. Find the year, month and day on which the greatest windspeed was recorded.
7. Find the average windspeed in January for each location.
You should be able to perform all of these operations without using a for
loop or other looping construct.
Bonus
~~~~~
1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)
2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.
Bonus Bonus
~~~~~~~~~~~
Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)
"""
import numpy as np

wind_data = np.loadtxt('wind.data')
dates = wind_data[:, :3]
winds = wind_data[:, 3:]


def stats_all_day_all_locations():
    min_wind_speed = np.min(winds)
    max_wind_speed = np.max(winds)
    mean_wind_speed = np.mean(winds)
    std_wind_speed = np.mean(winds)
    print('stats for all day all locations')
    print('min {}, max {}, mean {}, std {}'.format(min_wind_speed, max_wind_speed, mean_wind_speed, std_wind_speed))


def stats_for_each_location_for_all_day():
    min_wind_speed = np.min(winds, axis=0)
    max_wind_speed = np.max(winds, axis=0)
    mean_wind_speed = np.mean(winds, axis=0)
    std_wind_speed = np.mean(winds, axis=0)
    print(' each data point represents one location')
    print('min {}\nmax {}\nmean {}\nstd {}'.format(min_wind_speed.shape, max_wind_speed.shape, mean_wind_speed.shape, std_wind_speed.shape))


def stats_for_each_day_for_all_location():
    min_wind_speed = np.min(winds, axis=1)
    max_wind_speed = np.max(winds, axis=1)
    mean_wind_speed = np.mean(winds, axis=1)
    std_wind_speed = np.mean(winds, axis=1)
    print(' each data point represents one date')
    print('min {}\nmax {}\nmean {}\nstd {}'.format(min_wind_speed.shape, max_wind_speed.shape, mean_wind_speed.shape,
                                                   std_wind_speed.shape))


def location_having_greatest_wind_speed_on_each_day():
    max_wind_speed = np.argmax(winds, axis=1)
    print('max wind speed across locations on each day {}'.format(max_wind_speed))


def find_year_month_date_having_recorded_max_wind_speed():
    max_row, max_col = np.unravel_index(winds.argmax(), winds.shape)
    print('date when max wind speed occurred')
    print(dates[max_row, 0], dates[max_row, 1], dates[max_row, 2])

def average_wind_speed_in_jan():
    januraries = dates[:, 1] == 1
    print('mean temp in january')
    print(winds[januraries].mean(axis=0))

if __name__ == '__main__':
    stats_all_day_all_locations()
    stats_for_each_location_for_all_day()
    stats_for_each_day_for_all_location()
    location_having_greatest_wind_speed_on_each_day()
    find_year_month_date_having_recorded_max_wind_speed()
    average_wind_speed_in_jan()
