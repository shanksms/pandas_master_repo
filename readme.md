# Important pandas concepts
### resources
[pandas cookbook] (https://learning.oreilly.com/library/view/pandas-1-x-cookbook)
[Pandas interview question] (https://www.kaggle.com/getting-started/119445)

### Series object 
the Series is a one-dimensional labeled array for homogeneous data.  
A Series combines and expands the best features of Python’s native data structures.  
Like a list, it holds its values in a sequenced order. Like a dictionary, it assigns a key/label to each value.  
We gain the benefits of both of those objects plus more than 180 methods for data manipulation.
#### mathematical operations on Series object
##### cumsum
cumsum (cumulative sum) returns a new Series object with rolling sum
```python
import pandas as pd
import numpy as np
numbers = pd.Series([1, 2, 3, np.nan, 4, 5])
numbers.cumsum()
```
```shell script
Out [47] 0     1.0
         1     3.0
         2     6.0
         3     NaN
         4    10.0
         5    15.0
         dtype: float64
```
#### pct_change
The pct_change method returns pct difference from one Series value to another.  
The pct_change method defaults to a forward-fill strategy for missing values. With this strategy, pandas replaces  
a nan with the last valid value it encountered. Let’s invoke the method and then walk through the calculations:
```python
import pandas as pd
import numpy as np
numbers = pd.Series([1, 2, 3, np.nan, 4, 5])
numbers.pct_change()
```
```shell script
Out [50] 0         NaN
         1    1.000000
         2    0.500000
         3    0.000000
         4    0.333333
         5    0.250000
         dtype: float64
```
#### describe
describe is a handy method for summarize series. It provides avg, mean, std
#### Broadcasting
Pandas stores Series values in a numpy ndarray under the hood. When we use syntax like s + 3, pandas delegate the  
operation to numpy.  
Syntax like s1 + 3 means “Apply the same operation (add 3) to each value in the Series.” Each Series value gets  
the same message, much as every person listening to the same radio station at the same time hears the same song.

Broadcasting also describes mathematical operations between multiple Series objects. As a rule of thumb,  
pandas uses shared index labels to align values across different data structures. Let’s demonstrate this  
concept through an example. Let’s instantiate two Series with the same three-element index:
```python
import pandas as pd
s1 = pd.Series([1, 2, 3], index = ["A", "B", "C"])
s2 = pd.Series([4, 5, 6], index = ["A", "B", "C"])
print(s1 + s2)
```
```shell script
Out [74] A    5
         B    7
         C    9
         dtype: int64
```
Following is a pictorial representation of the operation.
![](images/broadcasting.PNG)  

#### mathematical operations on Series object - ends


### representing missing value in pandas
#### np.nan
nan stands for not a number. In pandas nan is used for missing values. if there is column which hold numeric value  
and if this column as missing value, pandas will automatically convert the datatype to float.

### convert a date time text to pandas Timestamp
```python
import pandas as pd
pd.to_datetime('2015-5-13')
```
### convert a series of text to Timestamp
```python
import pandas as pd
s = pd.Series(['12-5-2015', '14-1-2013',  '20/12/2017', '40/23/2017'])
pd.to_datetime(s, dayfirst=True, errors='coerce')
```

### convert pandas Timestamp to python datetime
```python
import pandas as pd
pd.to_datetime('2015-5-13').to_pydatetime()

```

### Strip time from Timestamp
```python
import pandas as pd
df = pd.DataFrame()
df['EffectiveDate'] = df['EffectiveDate'].dt.date
```

### convert a series to dataframe
```python
import pandas as pd
s = pd.Series([0.1, 0.2, 0.3])
df = pd.DataFrame({'weight': s})
```
