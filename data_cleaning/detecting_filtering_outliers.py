import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(1000, 4))
print(data.describe())
print('#' * 70)
# Suppose you wanted to find values in one of the columns exceeding 3 in absolute value:
col = data[2]
print(type(np.abs(col)))
print(col[np.abs(col) > 3] )
'''
To select all rows having a value exceeding 3 or –3, you can use the any method on a boolean DataFrame:
'''
print('#' * 70)
print(data[(np.abs(data) > 3).any(1)])