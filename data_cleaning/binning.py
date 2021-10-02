import pandas as pd
import numpy as np

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
'''
Let’s divide these into bins of 18 to 25, 26 to 35, 36 to 60, and finally 61 and older. 
To do so, you have to use cut, a function in pandas:
'''
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
print('#' * 70)
print(pd.value_counts(cats))
print('#' * 70)
group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

'''
A closely related function, qcut, bins the data based on sample quantiles. 
Depending on the distribution of the data, using cut will not usually 
result in each bin having the same number of data points. 
Since qcut uses sample quantiles instead, by definition you will obtain roughly equal-size bins:
'''
data = np.random.randn(1000)  # Normally distributed
cats = pd.qcut(data, 4)  # Cut into quartiles
print('#' * 70)
print(cats)
print('#' * 70)
print(cats.value_counts())