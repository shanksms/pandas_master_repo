# Pandas puzzles from orielly book

## Floating point errors
Look at the following code snippet:
```python
import pandas as pd
	
v = pd.Series([.1, 1., 1.1])
out = v * v
expected = pd.Series([.01, 1., 1.21])
if (out == expected).all():
    print('Math rocks!')
else:
    print('Please reinstall universe & reboot.')
```
it will print Please reinstall universe & reboot.  
To fix it, you should use np.allclose()  
```python
import pandas as pd
import numpy as np

v = pd.Series([.1, 1., 1.1])
out = v * v
expected = pd.Series([.01, 1., 1.21])
if np.allclose(out, expected):
    print('Math rocks!')
else:
    print('Please reinstall universe & reboot.')
```
Read following if you can.  
[what every programmer should know about floating point] (https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html)

## 	A value is trying to be set on a copy of a slice from a DataFrame. Try using .loc[row_indexer,col_indexer] = value instead
Observe the following code:
```python
import pandas as pd

df = pd.DataFrame([
    ['Bugs', True, 72.3],
    ['Daffy', False, 30.7],
    ['Tweety', True, 23.5],
    ['Elmer', False, 103.9],
], columns=['Customer', 'Member', 'Amount'])

df[df['Member']]['Amount'] *= 0.9
print(df)
```
This will print following warning.   
```shell script
 	discount.py:11: SettingWithCopyWarning:
 	A value is trying to be set on a copy of a slice from a DataFrame.
 	Try using .loc[row_indexer,col_indexer] = value instead
```
Fix is simple:  
```python
import pandas as pd

df = pd.DataFrame([
    ['Bugs', True, 72.3],
    ['Daffy', False, 30.7],
    ['Tweety', True, 23.5],
    ['Elmer', False, 103.9],
], columns=['Customer', 'Member', 'Amount'])

df.loc[df['Member'], 'Amount'] *= 0.9
print(df)
```
