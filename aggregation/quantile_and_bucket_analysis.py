import pandas as pd
import numpy as np

def get_stats(group):
    return {'min': group.min(), 'max': group.max(), 'count': group.count(), 'mean': group.mean()}

frame = pd.DataFrame({'data1': np.random.randn(1000), 'data2': np.random.randn(1000)})
quartiles = pd.cut(frame.data1, 4)
print(quartiles[:10])

grouped = frame.data2.groupby(quartiles)
print(grouped.apply(get_stats).unstack())
