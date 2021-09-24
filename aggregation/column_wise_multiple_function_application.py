import pandas as pd
from pathlib import Path
import numpy as np

path = Path(__file__).parent / "../tips.csv"

tips = pd.read_csv(path)
#add tip pct
tips['tip_pct'] = tips['tip'] / tips['total_bill']

grouped = tips.groupby(['day', 'smoker'])
grouped_pct = grouped['tip_pct']

print(grouped_pct.agg('mean'))
print('#'*70)
print(grouped_pct.agg(['mean', 'std']))

functions = ['count', 'mean', 'max']
result = grouped['tip_pct', 'total_bill'].agg(functions)
'''
As you can see, the resulting DataFrame has hierarchical columns, the same as you would get aggregating each 
column separately and using concat to glue the results together using the column names as the keys argument:
'''
print('#'*70)
print(result)
print('#'*70)
print(result['tip_pct'])

'''
Now, suppose you wanted to apply potentially different functions to one or more of the columns. To do this,
pass a dict to agg that contains a mapping of column names to any of the function specifications listed so far:
'''
print('#'*70)
print(grouped.agg({'tip': np.max, 'size': 'sum'}))
print('#'*70)
print(grouped.agg({'tip_pct' : ['min', 'max', 'mean', 'std'],'size' : 'sum'}))
'''
In all of the examples up until now, the aggregated data comes back with an index, potentially hierarchical, 
composed from the unique group key combinations. Since this isn’t always desirable, you can disable this behavior in 
most cases by passing as_index=False to groupby:
'''
