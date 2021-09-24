import pandas as pd
import numpy as np


'''
Using Python functions is a more generic way of defining a group mapping compared with a dict or Series.
Any function passed as a group key will be called once per index value, with the return values being used
as the group names. More concretely, consider the example DataFrame from the previous section,
which has people’s first names as index values. Suppose you wanted to group by the length of the names;
while you could compute an array of string lengths, it’s simpler to just pass the len function:
'''

people = pd.DataFrame(np.random.randn(5, 5),
                      columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

print(people.groupby(len).sum())

columns = pd.MultiIndex.from_arrays([['US', 'US', 'US', 'JP', 'JP'], [1, 3, 5, 1, 3]],
names=['cty', 'tenor'])

hier_df = pd.DataFrame(np.random.randn(4, 5), columns=columns)
print(type(hier_df))
print(hier_df)
print(hier_df.groupby(level='cty', axis=1).count())