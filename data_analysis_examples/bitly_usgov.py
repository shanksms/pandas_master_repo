import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path = 'bitly_usgov_example.txt'
records = [json.loads(line) for line in open(path)]
#records is a list of dictionaries
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()
print(tz_counts)
print('#' * 70)
clean_tz = frame['tz'].fillna('missing')
clean_tz[clean_tz == ''] = 'unknowns'
print(clean_tz.value_counts()[:10])
print('#' * 70)
subset = clean_tz.value_counts()[:10]
sns.barplot(y=subset.index, x = subset.values)
plt.show()

# Lets find out browsers used to shorten the urls
print(frame['a'][1])
print(frame['a'][50])
print('#' * 70)

# it seems, if we split it by space and take 0th element, that will be browser type
browsers = pd.Series([x.split(' ')[0] for x in frame['a'].dropna()])
print(browsers.value_counts()[:5])
print('#' * 70)

# decompose the top time zones into Windows and non-Windows users
cframe = frame[frame['a'].notnull()]
#cframe.loc[:, 'os'] = cframe.loc[:, 'a'].copy().apply(lambda x : 'Windows' if 'Windows' in x else 'Non Windows')
cframe['os'] = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
print(cframe['os'][:5])
print('#' * 70)
by_tz_os = cframe.groupby(['tz', 'os']).agg('size')
print(by_tz_os)
print('#' * 70)
by_tz_os_unstacked = by_tz_os.unstack().fillna(0)
print(by_tz_os_unstacked)
# Use to sort in ascending order. https://www.geeksforgeeks.org/python-pandas-series-argsort/
indexer = by_tz_os_unstacked.sum(1).argsort()
print('#' * 70)
print(indexer[:10])
count_subset = by_tz_os_unstacked.take(indexer[-10:])
print('#' * 70)
print(count_subset)
count_subset = count_subset.stack()
print('#' * 70)
print(count_subset)
count_subset.name = 'total'
print('#' * 70)
count_subset = count_subset.reset_index()
print(count_subset)
sns.barplot(x='total', y='tz', data=count_subset, hue='os')
plt.show()
