import pandas as pd
import numpy as np

s = pd.Series(np.random.random(6))
s[::2] = np.nan
print(s)
print('#'*70)
s = s.fillna(s.mean())
print(s)
states = ['Ohio', 'New York', 'Vermont', 'Florida',
     'Oregon', 'Nevada', 'California', 'Idaho']
group_key = ['East'] * 4 + ['West'] * 4
data = pd.Series(np.random.randn(8), index=states)
print('#'*70)
data[['Vermont', 'Nevada', 'Idaho']] = np.nan
print(data.groupby(group_key).mean())
print('#'*70)
fill_mean = lambda g : g.fillna(g.mean())
print(data.groupby(group_key).apply(fill_mean))