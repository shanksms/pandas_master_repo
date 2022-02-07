# Important pandas concepts
### resources
[pandas cookbook] (https://learning.oreilly.com/library/view/pandas-1-x-cookbook)
[Pandas interview question] (https://www.kaggle.com/getting-started/119445)

### filtering in dataframe and series
#### filtering by single condition
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
marias = employees["First Name"] == "Maria"
# following two lines are same
employees.loc[marias, :]
employees[marias]
```
employees["First Name"] == "Maria" returns a series of boolean (also known as boolean masks)
```shell script
Out [22] 0       False
         1       False
         2        True
         3       False
         4       False
                 ...
         996     False
         997     False
         998     False
         999     False
         1000    False
         Name: First Name, Length: 1001, dtype: bool
```
#### filtering by multiple condition
We can filter a DataFrame with multiple conditions by creating two independent Boolean Series and then declaring
the logical criterion that pandas should apply between them.
Suppose that we want to find all female employees who work on the business development team. Now pandas must look
for two conditions to select a row: a value of "Female" in the Gender column and a value of "Business Dev" in the Team
column. The two criteria are independent, but both must be met. Here’s a quick reminder of how AND logic works with two conditions:
![](images/multiple_filtering_condition.PNG)

##### and condition
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
marias = employees["First Name"] == "Maria"
is_female = employees["Gender"] == "Female"
in_biz_dev = employees["Team"] == "Business Dev"
employees[is_female & in_biz_dev].head()
employees.loc[is_female & in_biz_dev , :].head()

```
```shell script
Out [33]
 
   First Name  Gender Start Date  Salary   Mgmt          Team
9     Frances  Female 2002-08-08  139852   True  Business Dev
33       Jean  Female 1993-12-18  119082  False  Business Dev
36     Rachel  Female 2009-02-16  142032  False  Business Dev
38  Stephanie  Female 1986-09-13   36844   True  Business Dev
61     Denise  Female 2001-11-06  106862  False  Business Dev
```

##### or condition
We can also extract rows if they fit one of several conditions. Not all conditions have to be true,
but at least one does. Here’s a quick reminder of how OR logic works with two conditions:
![](images/multiple_filtering_or_condition.PNG)
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
marias = employees["First Name"] == "Maria"
earning_below_40k = employees["Salary"] < 40000
started_after_2015 = employees["Start Date"] > "2015-01-01"
employees[earning_below_40k | started_after_2015].head()
employees.loc[earning_below_40k | started_after_2015 , :].head()

```
##### inversion with tilda ~
```python
import pandas as pd
my_series = pd.Series([True, False, True])
print(my_series)
print(~my_series)
```
```shell script
Out [37] 0     True
         1    False
         2     True
         dtype: bool
  
Out [38] 0    False
         1     True
         2    False
         dtype: bool
```
##### The isin method
isin method accepts an iterable of elements (list, tuple, Series, and so on) and returns a Boolean Series.
True denotes that pandas found the row’s value among the iterable’s values, and False denotes that it did not.
When we have the Series, we can use it to filter the DataFrame in the usual manner. The next example achieves the same
result set:
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
all_star_teams = ["Sales", "Legal", "Marketing"]
on_all_star_teams = employees["Team"].isin(all_star_teams)
employees[on_all_star_teams].head()
```
##### The isnull and notnull methods
Pandas considers the NaN, NaT and None values to be null as well. The next example invokes the isnull method on the Start Date column:
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
employees["Team"].isnull().head()
employees["Team"].notnull().head()
```
```shell script
Out [48] 0    False
         1     True
         2    False
         3    False
         4    False
         Name: Team, dtype: bool
```
The notnull method returns the inverse Series, one in which True indicates that a row’s value is present. The following
output communicates that indices 0, 2, 3, and 4 do not have missing values:

### reducing memory footprint
Let's checkout following dataframe
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
employees.info()

```
```shell script
Out [3]
 
  First Name  Gender  Start Date    Salary   Mgmt       Team
0    Douglas    Male  1993-08-06       NaN   True  Marketing
1     Thomas    Male  1996-03-31   61933.0   True        NaN
2      Maria  Female         NaT  130590.0  False    Finance
3      Jerry     NaN  2005-03-04  138705.0   True    Finance
4      Larry    Male  1998-01-24  101004.0   True         IT
 
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   First Name  933 non-null    object
 1   Gender      854 non-null    object
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      999 non-null    float64
 4   Mgmt        933 non-null    object
 5   Team        957 non-null    object
dtypes: datetime64[ns](1), float64(1), object(4)
message usage: 47.0+ KB
```
Mgmt series type is object. Since it only contains True or False we can convert the type to boolean which is light weight.
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
employees.info()
employees["Mgmt"] = employees["Mgmt"].astype(bool)
employees.info()
```
```shell script
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1001 entries, 0 to 1000
Data columns (total 6 columns):
 #   Column      Non-Null Count  Dtype
---  ------      --------------  -----
 0   First Name  933 non-null    object
 1   Gender      854 non-null    object
 2   Start Date  999 non-null    datetime64[ns]
 3   Salary      999 non-null    float64
 4   Mgmt        1001 non-null   bool
 5   Team        957 non-null    object
dtypes: bool(1), datetime64[ns](1), float64(1), object(3)
memory usage: 40.2+ KB
```
Next, let’s transition to the Salary column. If we open the raw CSV file, we can see that its values are stored as whole numbers:
```shell script
First Name,Gender,Start Date,Salary,Mgmt,Team
Douglas,Male,8/6/93,,True,Marketing
Thomas,Male,3/31/96,61933,True,
Maria,Female,,130590,False,Finance
Jerry,,3/4/05,138705,True,Finance
```
In employees, however, pandas stores the Salary values at floats. To support the NaNs throughout the column, pandas
converts the integers to floating-point numbers—a technical requirement of the library that we observed in earlier chapters.
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
employees["Salary"] = employees["Salary"].fillna(0).astype(int)
```
When there few unique numbers in a column, we can convert that column to Category
```python
import pandas as pd
employees = pd.read_csv("employees.csv", parse_dates = ["Start Date"]).head()
employees.nunique()
employees["Gender"] = employees["Gender"].astype("category")
```
```shell script
Out [14] First Name    200
         Gender          2
         Start Date    971
         Salary        995
         Mgmt            2
         Team           10
         dtype: int64
```
With above changes, we can reduce memory footprints by 40%
### Dataframe object
The pandas DataFrame is a two-dimensional table of data with rows and columns.  
As with a Series, pandas assigns an index label and an index position to each DataFrame row.  
Pandas also assigns a label and a position to each column. The DataFrame is two-dimensional because  
it requires two points of reference—a row and a column—to isolate a value from the data set.  
Figure 4.1 displays a visual example of a pandas DataFrame. A DataFrame can hold multiple columns of data.
It’s helpful to think of the column headers as a second index. City, Country, and Population are three index labels on  
the column axis; pandas assigns them the index positions 0, 1, and 2, respectively.
It’s also helpful to think of a DataFrame as being a collection of Series objects with a common index.  
In this example, the five columns in nba (Name, Team, Position, Birthday, and Salary) share the same row index.  
Let’s get to work exploring the DataFrame.
![](images/dataframe.PNG)  

#### creating dataframe from dictionary
```python
import pandas as pd
city_data = {
            "City": ["New York City", "Paris", "Barcelona", "Rome"],
            "Country": ["United States", "France", "Spain", "Italy"],
            "Population": [8600000, 2141000, 5515000, 2873000]
        }
city_df = pd.DataFrame(city_data)
# below code will transpose the dataframe
city_df.T
```

#### using parse_dates attribute to change the date to type datetime
```python
import pandas as pd
pd.read_csv("nba.csv", parse_dates = ["Birthday"])
```

#### finding data types of each column
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.dtypes
```
```shell script
Out [13] Name                object
         Team                object
         Position            object
         Birthday    datetime64[ns]
         Salary               int64
         dtype: object
```
#### find n smallest players
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.dtypes
nba.nsmallest(n = 3, columns = ["Birthday"])
```
```shell script
Out [34]
 
              Name             Team Position   Birthday   Salary
98    Vince Carter    Atlanta Hawks       PF 1977-01-26  2564753
196  Udonis Haslem       Miami Heat        C 1980-06-09  2564753
262    Kyle Korver  Milwaukee Bucks       PF 1981-03-17  6004753
```

#### sort by column values 
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.sort_values("Name")
nba.sort_values(by = "Name")
```
#### sort by row and column
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.sort_index().head() # by row index
# following two lines are same.
nba.sort_index(axis = "columns").head() # sort by columns
nba.sort_index(axis = 1).head()
```

#### select columns based on datatypes
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.select_dtypes(include = "object")
```

#### loc and iloc
1. The loc attribute extracts a row by label. We call attributes such as loc accessors because  
they access a piece of data. Type a pair of square brackets immediately after loc and pass in the target index label.
2. The iloc (index location) accessor extracts rows by index position, which is helpful when the position of our rows  
has significance in our data set. The syntax is similar to the one we used for loc. Enter a pair of square brackets
after iloc, and pass in an integer. Pandas will extract the row at that index.

Both the loc and iloc attributes accept a second argument representing the column(s) to extract.
If we’re using loc, we have to provide the column name. If we’re using iloc, we have to provide the column position.
The next example uses loc to pull the value at the intersection of the "Giannis Antetokounmpo" row and the Team column

```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.loc["Giannis Antetokounmpo", "Team"]
#following will select all the rows and Team column
nba.loc[:, 'Team']

```
#### resetting the index
reset_index function moves the current index to a column and creates a new monotonic integer index.
```python
import pandas as pd
nba = pd.read_csv("nba.csv", parse_dates = ["Birthday"])
nba.reset_index().head()
```
### Dataframe object - ends

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
##### pct_change
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
##### describe
describe is a handy method for summarize series. It provides avg, mean, std
##### Broadcasting
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

#### converting series to list, dict etc
```python
import pandas as pd
cities = pd.Series(['Newyork', 'California', 'Washington'])
print(dict(cities))
print(list(cities))
```
### Series - ends 

### representing missing value in pandas
#### np.nan
nan stands for not a number. In pandas nan is used for missing values. if there is column which hold numeric value  
and if this column as missing value, pandas will automatically convert the datatype to float.
#### np.NaT for missing dates
NaT stands for Not a time.

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
### multi index
So far on our pandas journey, we’ve explored the one-dimensional Series and the two-dimensional DataFrame.
The number of dimensions is the number of reference points we need to extract a value from a data structure.
We need only one label or one index position to locate a value in a Series. We need two reference points to locate a
value in a DataFrame: a label/index for the rows and a label/index for the columns. Can we expand beyond two dimensions?
Absolutely! Pandas supports data sets with any number of dimensions through the use of a MultiIndex.  
A MultiIndex is an index object that holds multiple levels.
#### Create multindexes manually
Let’s say we want to model a street address. An address typically includes a street name, city, town, and zip code.
We could store these four elements in a tuple:
```python
import pandas as pd
addresses = [
            ("8809 Flair Square", "Toddside", "IL", "37206"),
            ("9901 Austin Street", "Toddside", "IL", "37206"),
            ("905 Hogan Quarter", "Franklin", "IL", "37206"),
        ]
row_index = pd.MultiIndex.from_tuples(
            tuples = addresses,
            names = ["Street", "City", "State", "Zip"]
        )
column_index = pd.MultiIndex.from_tuples(
             [
                 ("Culture", "Restaurants"),
                 ("Culture", "Museums"),
                 ("Services", "Police"),
                 ("Services", "Schools"),
             ]
         )
 
data = [
            ["C-", "B+", "B-", "A"],
            ["D+", "C", "A", "C+"],
            ["A-", "A", "D+", "F"]
        ]
pd.DataFrame(
             data = data, index = row_index, columns = column_index
         )


```
To summarize, a MultiIndex is a storage container in which each label holds multiple values.A level consists of the
values at the same position across the labels.

