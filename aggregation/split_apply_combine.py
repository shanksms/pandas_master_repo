import pandas as pd
from pathlib import Path
import numpy as np


def top(df, n=5, column='tip_pct'):
    return df.sort_values(by=column).tail(n)

path = Path(__file__).parent / "../tips.csv"

tips = pd.read_csv(path)
#add tip pct
tips['tip_pct'] = tips['tip'] / tips['total_bill']
print(top(tips))
print('#' * 70)
print(tips.groupby('smoker').apply(top))
print('#' * 70)
print(tips.groupby(['smoker', 'day']).apply(top, n=1, column='total_bill'))