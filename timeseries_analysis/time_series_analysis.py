import pandas as pd
# Get the below file from location
# https://github.com/PacktPublishing/Pandas-Cookbook-Second-Edition/blob/master/data/crime.h5

crime = pd.read_hdf('crime.h5', 'crime')
#print(crime)
crime = crime.set_index('REPORTED_DATE')
print(crime.head())
# As usual, it is possible to select all the rows equal to a single index by passing that value to the .loc attribute:
print(crime.loc['2016-05-12 16:45:00'])
# With a Timestamp in the index, it is possible to select all rows that partially match an index value.
# For instance, if we wanted all the crimes from May 5, 2016, we would select it as follows:

'''
below also work fine
>>> crime.loc['2016-05'].shape
(8012, 7)
>>> crime.loc['2016'].shape
(91076, 7)
>>> crime.loc['2016-05-12 03'].shape
(4, 7)
'''
# In addition to selection, you may use the slice notation to select a precise range of data.
# This example will include all values starting from March 4, 2015 through the end of January 1, 2016:
print(crime.loc['2015-3-4':'2016-1-1'].sort_index())

# One of the features of hdf5 files is their ability to preserve the data types of each column,
# which reduces the memory required. In this case, three of these columns are stored as a pandas
# category instead of as an object. Storing them as objects will lead to a four times increase in memory usage:
mem_cat = crime.memory_usage().sum()
mem_obj = (crime
    .astype({'OFFENSE_TYPE_ID':'object',
             'OFFENSE_CATEGORY_ID':'object',
            'NEIGHBORHOOD_ID':'object'}) 
    .memory_usage(deep=True)
    .sum()
 )
mb = 2 ** 20

print(round(mem_cat / mb, 1), round(mem_obj / mb, 1))
print(crime.index[:2])

'''
Filtering columns with time data
'''
crime = pd.read_hdf('crime.h5', 'crime')
print('#' * 80)
print(crime.dtypes)
# below works
print(crime.loc[crime.REPORTED_DATE == '2016-05-12 16:45:00', ])
# Select all rows with a partial date match. If we try this with the equality operator, it fails.
# We do not get an error, but there are no rows returned:
print('#' * 80)
print(crime.loc[crime.REPORTED_DATE == '2016-05-12', ])

# If we want a partial date match, we can use the .between method, which supports partial date strings. Note that
# the start and end dates (the parameter names are left and right respectively) are inclusive by default.
# If there were a row with a date on midnight May 13, 2016, it would be included here:
print('#' * 80)
print(crime.loc[crime.REPORTED_DATE.between('2016-05-12', '2016-05-13'), ])

# Because .between supports partial date strings, we can replicate most of the slicing functionality of the previous
# section with it. We can match just a month, year, or hour of the day: