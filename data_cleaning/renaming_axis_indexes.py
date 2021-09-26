import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=['Ohio', 'Colorado', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
# Like a Series, the axis indexes have a map method:
data.index = data.index.map(lambda x : x[:4].upper())
print('#' * 70)
print(data)
