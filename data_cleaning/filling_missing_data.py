import pandas as pd
import numpy as np



df = pd.DataFrame(np.random.randn(6, 3))
df.loc[:4, 1] = np.nan
df.loc[:2, 2] = np.nan
print(df)
print('#' * 70)
print(df.fillna(0))
print('#' * 70)
# Calling fillna with a dict, you can use a different fill value for each column:
print(df.fillna({1: 0.5, 2: 0}))
