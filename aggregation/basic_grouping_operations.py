
import pandas as pd
import numpy as np

df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'],
              'key2' : ['one', 'two', 'one', 'two', 'one'],
               'data1' : np.random.randn(5),
               'data2': np.random.randn(5),
              })
'''
below is same since key is found in the dataframe
df.groupby(df['key1']).mean()['data1']
df.groupby('key1').mean()['data1']
'''
print(df.groupby(df['key1']).mean()['data1'])
means = df.groupby([df['key1'], df['key2']]).mean()
print(means)
print(means['data1'].unstack())

states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
years = np.array([2005, 2005, 2006, 2005, 2006])
print(df['data1'].groupby([states, years]).mean())
