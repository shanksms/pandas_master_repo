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

#### refer to multiindex_example.py for creating multiindex dataframe from csv

#### sorting a multi index
When we invoke the method on a MultiIndex DataFrame, pandas sorts all levels in ascending order and proceeds from
the outside in. In the next example, pandas sorts the State-level values first, then the City-level values, and finally
the Street-level values:

```python
import pandas as pd

neighborhoods = pd.read_csv(
    "neighborhoods.csv",
    index_col=[0, 1, 2],
    header=[0, 1]
)
neighborhoods.sort_index()
```
```shell script
Category                                  Culture         Services
Subcategory                           Restaurants Museums   Police Schools
State City            Street                                              
AK    Rowlandchester 386 Rebecca ...          C-      A-       A+        C
      Scottstad      082 Leblanc ...           D      C-        D       B+
                     114 Jones Ga...          D-      D-        D        D
      Stevenshire    238 Andrew Rue           D-       A       A-       A-
AL    Clarkland      430 Douglas ...           A       F       C+       B+
 ...       ...           ...                  ...     ...      ...     ...
WY    Lake Nicole    754 Weaver T...           B      D-        B        D
                     933 Jennifer...           C      A+       A-        C
      Martintown     013 Bell Mills           C-       D       A-       B-
      Port Jason     624 Faulkner...          A-       F       C+       C+
      Reneeshire     717 Patel Sq...           B      B+        D        A
 
251 rows × 4 columns
```
We can also pass ascending as list. Following example will sort first level in ascending order, second level in descending order
and so on.
```python
import pandas as pd

neighborhoods = pd.read_csv(
    "neighborhoods.csv",
    index_col=[0, 1, 2],
    header=[0, 1]
)
neighborhoods.sort_index(ascending = [True, False, True]).head()

```

#### selecting with multilevel index


### Working with text data
#### removing whitespaces and letter casing
If you run following code snippet, you will see whitespaces.
```python
import pandas as pd
inspections = pd.read_csv("chicago_food_inspections.csv")
print(inspections)
print(inspections["Name"].head().values)
```
```shell script
                                      Name             Risk
0                  MARRIOT MARQUIS CHICAGO    Risk 1 (High)
1                               JETS PIZZA  Risk 2 (Medium)
2                                ROOM 1520     Risk 3 (Low)
3                  MARRIOT MARQUIS CHICAGO    Risk 1 (High)
4                               CHARTWELLS    Risk 1 (High)
     ...                                  ...                 ...
153805                           WOLCOTT'S    Risk 1 (High)
153806        DUNKIN DONUTS/BASKIN-ROBBINS  Risk 2 (Medium)
153807                            Cafe 608    Risk 1 (High)
153808                         mr.daniel's    Risk 1 (High)
153809                          TEMPO CAFE    Risk 1 (High)
 
153810 rows × 2 columns

Out [4] array([' MARRIOT MARQUIS CHICAGO   ', ' JETS PIZZA ',
               '   ROOM 1520 ', '  MARRIOT MARQUIS CHICAGO  ',
               ' CHARTWELLS   '], dtype=object)
```
The Series object’s str attribute exposes a StringMethods object, a powerful toolbox of methods for working with strings:
```shell script
In  [5] inspections["Name"].str
Out [5] <pandas.core.strings.StringMethods at 0x122ad8510>
```
Any time we’d like to perform string manipulations, we invoke a method on the StringMethods object rather than the
Series itself. Some methods work like Python’s native string methods, whereas other methods are exclusive to pandas.

```python
import pandas as pd
inspections = pd.read_csv("chicago_food_inspections.csv")
inspections["Name"] = inspections["Name"].str.strip()
```
Lets say you'like to perform strip operation on all the columns.
```python
import pandas as pd
inspections = pd.read_csv("chicago_food_inspections.csv")
for column in inspections.columns:
    inspections[column] = inspections[column].str.strip()
```
All of Python’s character casing methods are available on the StringMethods object. The lower method, for example,
lowercases all string characters:
```shell script
inspections["Name"].str.lower().head()
```
#### rename columns
```shell script
df.columns = df.columns.str.replace("_", "")
```

### reshaping and pivoting
Reshaping a dataset means manipulating it to different shapes, one that tells a story which could not, otherwise,  
gleaned from the original presentation.

#### Wide and narrow data
A wide data set increases in width; it grows out. A narrow/long/tall data set increases in height; it grows down.
```shell script
   Weekday  Miami  New York
0   Monday    100        65
1  Tuesday    105        70
```
Consider the variables, the measurements that vary. One might think that the only variables in this data set are the  
weekdays and the temperatures. But an additional variable is hiding in the column names: the city. This data set stores  
the same variable—temperature—across two columns instead of one. The Miami and New York headers do not describe the data  
their columns store—that is, 100 is not a type of Miami in the same way that Monday is a type of Weekday. The data set has  
hidden the varying cities variable by storing it in the column headers. We can categorize this table as being a wide  
data set. A wide data set expands horizontally.
Suppose that we introduced temperature measurements for two more cities. We would have to add two new columns for the  
same variable: the temperature. Notice the direction in which the data set expands. The data grows wider, not taller:
```shell script
   Weekday  Miami  New York  Chicago  San Francisco
0   Monday    100        65       50             60
1  Tuesday    105        70       58             62
```
A narrow data set grows vertically. A narrow format makes it easier to manipulate existing data and to add new records.  
Each variable is isolated to a single column. Compare the first table in this section with the following table:
```shell script
   Weekday           City  Temperature
0   Monday          Miami          100
1   Monday       New York           65
2   Monday        Chicago           50
3   Monday  San Francisco           60
4  Tuesday          Miami          105
5  Tuesday       New York           70
6  Tuesday        Chicago           58
7  Tuesday  San Francisco           62
```
#### pivot_table method
We follow four steps to create a pivot table:  
1. Select the column(s) whose values we want to aggregate.
2. Choose the aggregation operation to apply to the column(s).
3. Select the column(s) whose values will group the aggregated data into categories.
4. Determine whether to place the groups on the row axis, the column axis, or both axes.

```python
import pandas as pd
print(pd.read_csv("sales_by_employee.csv", parse_dates = ["Date"]))

```
```shell script
   Date   Name       Customer  Revenue  Expenses
0  1/1/20  Oscar  Logistics XYZ     5250       531
1  1/1/20  Oscar    Money Corp.     4406       661
2  1/2/20  Oscar     PaperMaven     8661      1401
3  1/3/20  Oscar    PaperGenius     7075       906
4  1/4/20  Oscar    Paper Pound     2524      1767
```
```shell script
In  [7] sales.pivot_table(
            index = "Date", values = "Revenue", aggfunc = "sum"
        )
 
Out [7]
 
            Revenue
Date               
2020-01-01    25761
2020-01-02    36515
2020-01-03    29195
2020-01-04    19740
2020-01-05    19339
```

```shell script
In  [8] sales.pivot_table(
            index = "Date",
            columns = "Name",
            values = "Revenue",
            aggfunc = "sum"
        )
 
Out [8]
 
Name          Creed   Dwight     Jim  Michael   Oscar
Date                                                 
2020-01-01   4430.0   2639.0  1864.0   7172.0  9656.0
2020-01-02  13214.0      NaN  8278.0   6362.0  8661.0
2020-01-03      NaN  11912.0  4226.0   5982.0  7075.0
2020-01-04   3144.0      NaN  6155.0   7917.0  2524.0
2020-01-05    938.0   7771.0     NaN   7837.0  2793.0
```

#### stacking and unstacking
stack moves an index level from column axis to row axis.  
unstack moves an inner index level from row axis to column axis.  
```shell script
In  [17] sales.head()
 
Out [17]
 
        Date   Name       Customer  Revenue  Expenses
0 2020-01-01  Oscar  Logistics XYZ     5250       531
1 2020-01-01  Oscar    Money Corp.     4406       661
2 2020-01-02  Oscar     PaperMaven     8661      1401
3 2020-01-03  Oscar    PaperGenius     7075       906
4 2020-01-04  Oscar    Paper Pound     2524      1767

```
Let’s pivot sales to organize revenue by employee name and date. We’ll place dates on the column axis and names on the row axis  

```shell script
In  [18] by_name_and_date = sales.pivot_table(
             index = "Name",
             columns = "Date",
             values = "Revenue",
             aggfunc = "sum"
         )
 
         by_name_and_date.head(2)
 
Out [18]
 
Date    2020-01-01  2020-01-02  2020-01-03  2020-01-04  2020-01-05
Name                                                              
Creed       4430.0     13214.0         NaN      3144.0       938.0
Dwight      2639.0         NaN     11912.0         NaN      7771.0
```

```shell script
In  [19] by_name_and_date.stack().head(7)
 
Out [19]
 
Name    Date
Creed   2020-01-01     4430.0
        2020-01-02    13214.0
        2020-01-04     3144.0
        2020-01-05      938.0
Dwight  2020-01-01     2639.0
        2020-01-03    11912.0
        2020-01-05     7771.0
dtype: float64
```

The complementary unstack method moves an index level from the row axis to the column axis. Consider the following pivot  
table, which groups revenue by customer and salesman. The row axis has a two-level MultiIndex, and the column axis has a regular index:
```shell script
In  [20] sales_by_customer = sales.pivot_table(
             index = ["Customer", "Name"],
             values = "Revenue",
             aggfunc = "sum"
         )
 
         sales_by_customer.head()
 
Out [20]
 
                           Revenue
Customer          Name            
Average Paper Co. Creed      13214
                  Jim         2287
Best Paper Co.    Dwight      2703
                  Michael    15754
Logistics XYZ     Dwight      9209
```

The unstack method moves the innermost level of the row index to the column index:  
```shell script
In  [21] sales_by_customer.unstack()
 
Out [21]
 
                   Revenue
Name                 Creed  Dwight     Jim  Michael   Oscar
Customer                                                   
Average Paper Co.  13214.0     NaN  2287.0      NaN     NaN
Best Paper Co.         NaN  2703.0     NaN  15754.0     NaN
Logistics XYZ          NaN  9209.0     NaN   7172.0  5250.0
Money Corp.         5368.0     NaN  8278.0      NaN  4406.0
Paper Pound            NaN  7771.0  4226.0      NaN  5317.0
PaperGenius            NaN  2639.0  1864.0  12344.0  7075.0
PaperMaven          3144.0     NaN  3868.0      NaN  8661.0
```

#### melting a dataset
A pivot table aggregates the values in a data set. In this section, we’ll learn how to do the opposite:  
break an aggregated collection of data into an unaggregated one.

Let’s apply our wide-versus-narrow framework to the sales DataFrame. Here’s an effective strategy to figure out whether  
a data set is in narrow format: navigate across one row of values, and ask each cell whether its value is a single  
measurement of the variable that the column header is describing. Here’s the first row of sales:
```shell script
In  [22] sales.head(1)
 
Out [22]
 
        Date   Name       Customer  Revenue  Expenses
0 2020-01-01  Oscar  Logistics XYZ     5250       531
```

In the previous example, "2020-01-01" is a Date, "Oscar" is a Name, "Logistics XYZ" is a Customer, 5250 is a Revenue  
amount, and 531 is an Expenses amount. The sales DataFrame is an example of a narrow data set. Each row value represents  
a single observation for a given variable. No variable repeats across multiple columns.  
The next data set, video_game_sales.csv, is a listing of regional sales for more than 16,000 video games.  
Each row includes the game’s name as well as the number of units sold (in millions) in the North America (NA), Europe (EU),  
Japan (JP), and other (Other) regions:

```shell script
In  [23] video_game_sales = pd.read_csv("video_game_sales.csv")
         video_game_sales.head()
 
Out [23]
 
                  Name     NA     EU     JP  Other
0           Wii Sports  41.49  29.02   3.77   8.46
1    Super Mario Bros.  29.08   3.58   6.81   0.77
2       Mario Kart Wii  15.85  12.88   3.79   3.31
3    Wii Sports Resort  15.75  11.01   3.28   2.96
4  Pokemon Red/Poke...  11.27   8.89  10.22   1.00
```

The first cell is fine; "Wii Sports" is an example of a Name. The next four cells are problematic. 41.49 is not a type  
of NA or a measurement of NA. NA (North America) is not a variable whose values vary throughout its column. The NA column’s  
real piece of variable data is the sales numbers. NA represents the region for those sales numbers—a separate and distinct variable.
Thus, video_game_sales stores its data in wide format. Four columns (NA, EU, JP, and Other) store the same data point: the number  
of units sold. If we added more regional sales columns, the data set would grow horizontally. If we can group multiple  
column headers in a common category, it is a hint that the data set is storing its data in wide format.  
Pandas melts a DataFrame with the melt method. (Melting is the process of converting a wide data set to a narrow one.)  
The method accepts two primary parameters:
The id_vars parameter sets the identifier column, the column for which the wide data set aggregates data. Name is the identifier  
column in video_game_sales. The data set aggregates sales per video game.
The value_vars parameter accepts the column(s) whose values pandas will melt and store in a new column.

```shell script
In  [26] regional_sales_columns = ["NA", "EU", "JP", "Other"]

In  [27] video_game_sales_by_region = video_game_sales.melt(
             id_vars = "Name",
             value_vars = regional_sales_columns,
             var_name = "Region",
             value_name = "Sales"
         )
 
         video_game_sales_by_region.head()
 
Out [27]
 
                       Name Region  Sales
0                Wii Sports     NA  41.49
1         Super Mario Bros.     NA  29.08
2            Mario Kart Wii     NA  15.85
3         Wii Sports Resort     NA  15.75
4  Pokemon Red/Pokemon Blue     NA  11.27
```
#### Exploding a list of values
Sometimes, a data set stores multiple values in the same cell. We may want to break up the data cluster so that each  
row stores a single value. Consider recipes.csv, a collection of three recipes, each of which has a name and an ingredients  
list. The ingredients are stored in a single comma-separated string:
```shell script
In  [29] recipes = pd.read_csv("recipes.csv")
         recipes
 
Out [29]
 
                    Recipe                              Ingredients
0   Cashew Crusted Chicken  Apricot preserves, Dijon mustard, cu...
1      Tomato Basil Salmon  Salmon filets, basil, tomato, olive ...
2  Parmesan Cheese Chicken  Bread crumbs, Parmesan cheese, Itali...

In  [31] recipes["Ingredients"] = recipes["Ingredients"].str.split(",")
         recipes
 
Out [31]
 
                    Recipe                              Ingredients
0   Cashew Crusted Chicken  [Apricot preserves,  Dijon mustard, ...
1      Tomato Basil Salmon  [Salmon filets,  basil,  tomato,  ol...
2  Parmesan Cheese Chicken  [Bread crumbs,  Parmesan cheese,  It...
```

Now, how can we spread out each list’s values across multiple rows? The explode method creates a separate row for  
each list element in a Series. We invoke the method on a DataFrame and pass in the column with lists:
```shell script
In  [32] recipes.explode("Ingredients")
 
Out [32]
 
                   Recipe         Ingredients
0  Cashew Crusted Chicken   Apricot preserves
0  Cashew Crusted Chicken       Dijon mustard
0  Cashew Crusted Chicken        curry powder
0  Cashew Crusted Chicken     chicken breasts
0  Cashew Crusted Chicken             cashews
1     Tomato Basil Salmon       Salmon filets
1     Tomato Basil Salmon               basil
1     Tomato Basil Salmon              tomato
1     Tomato Basil Salmon           olive oil
1     Tomato Basil Salmon     Parmesan cheese
2  Simply Parmesan Cheese        Bread crumbs
2  Simply Parmesan Cheese     Parmesan cheese
2  Simply Parmesan Cheese   Italian seasoning
2  Simply Parmesan Cheese                 egg
2  Simply Parmesan Cheese     chicken breasts
```






