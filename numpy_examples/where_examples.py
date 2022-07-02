import numpy as np

arr = np.array([11, 12, 13, 14])
high_values = ['High', 'High', 'High', 'High']
low_values = ['Low', 'Low', 'Low', 'Low']

print(np.where(arr > 12, high_values, low_values))
print(np.where(arr > 12))