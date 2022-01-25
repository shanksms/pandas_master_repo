# Important pandas concepts
### resources
[pandas cookbook] (https://learning.oreilly.com/library/view/pandas-1-x-cookbook)
[Pandas interview question] (https://www.kaggle.com/getting-started/119445)

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
