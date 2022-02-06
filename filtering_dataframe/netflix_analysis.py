import pandas as pd
"""
The netflix.csv data set is a collection of almost 6,000 titles that were available to watch in November 2019 on the
video streaming service Netflix. It includes four columns: the video’s title, director, the date Netflix added it, and
its type/category. The director and date_added columns contain missing values.
Using the skills you learned in this chapter, solve the following challenges:

1. Optimize the data set for limited memory use and maximum utility.

2. Find all rows with a title of "Limitless".

3. Find all rows with a director of "Robert Rodriguez" and a type of "Movie".

4. Find all rows with either a date_added of "2019-07-31" or a director of "Robert Altman".

5. Find all rows with a director of "Orson Welles", "Aditya Kripalani", or "Sam Raimi".

6. Find all rows with a date_added value between May 1, 2019 and June 1, 2019.

7. Drop all rows with a NaN value in the director column.

8. Identify the days when Netflix added only one movie to its catalog.


"""


netflix_df = pd.read_csv('netflix.csv', parse_dates=['date_added'])
print(netflix_df.info())
#print(netflix_df.head())
print('#' * 80)
print('reduce memory footprint')
netflix_df['type'] = netflix_df.loc[:, 'type'].astype('category')
#netflix_df['type'] = netflix_df['type'].astype('category')
print(netflix_df.info())
print('#' * 80)
print('print rows with tile limitless')
limitless = netflix_df.loc[:, 'title'] == 'Limitless'
print(netflix_df.loc[limitless, :])


