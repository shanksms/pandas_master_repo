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