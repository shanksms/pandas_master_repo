import pandas as pd
import numpy as np

string_data = pd.Series(['aardvark', 'artichoke', np.nan, 'avocado'])
print('#' * 70)
print(string_data.isnull())
# The built-in Python None value is also treated as np.nan in object arrays:
string_data[0] = None
print('#' * 70)
print(string_data.isnull())
# drop np.nan. similar to data[data.notnull()]
data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print('#' * 70)
print(data.dropna())
'''
With DataFrame objects, things are a bit more complex. 
You may want to drop rows or columns that are all np.nan or only those 
containing any np.nans. dropnp.nan by default drops any row containing a missing value:
'''
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
cleaned = data.dropna()
print('#' * 70)
print(data)
print('#' * 70)
print(cleaned)
# Passing how='all' will only drop rows that are all NA:
print('#' * 70)
print(data.dropna(how='all'))
'''
A related way to filter out DataFrame rows tends to concern time series data. 
Suppose you want to keep only rows containing a certain number of observations. 
You can indicate this with the thresh argument:
'''
df = pd.DataFrame(np.random.randn(7, 3))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
print('#' * 70)
print(df)
print('#' * 70)
print(df.dropna())
print('#' * 70)
print(df.dropna(thresh=2))
