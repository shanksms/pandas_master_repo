import pandas as pd
import numpy as np


def test_apply(row_or_column):
    print(row_or_column)


df = pd.DataFrame({'column1': [1, 2], 'column2': [3, 4]})
print(df)
# when we use axis=1, apply calls test_method for each row
df.apply(test_apply, axis=1)
# when we use axis=0, apply calls test_method for each row
df.apply(test_apply, axis=0)
print('#' * 70)
print(df.sum(axis=1))
print('#' * 70)
print(df.sum(axis=0))

