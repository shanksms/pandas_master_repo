import pandas as pd

"""
This coding challenge’s data set, cereals.csv, is a listing of 80 popular breakfast cereals. Each row includes a cereal’s name, manufacturer, type, calories, grams of fiber, and grams of sugar. Let’s take a look:

In  [45] cereals = pd.read_csv("cereals.csv")
         cereals.head()
 
Out [45]
 
                  Name    Manufacturer  Type  Calories  Fiber  Sugars
0            100% Bran         Nabisco  Cold        70   10.0       6
1    100% Natural Bran     Quaker Oats  Cold       120    2.0       8
2             All-Bran       Kellogg's  Cold        70    9.0       5
3  All-Bran with Ex...       Kellogg's  Cold        50   14.0       0
4       Almond Delight  Ralston Purina  Cold       110    1.0       8



Here are the challenges:

Group the cereals, using the Manufacturer column’s values.

Determine the total number of groups, and the number of cereals per group.

Extract the cereals that belong to the manufacturer/group "Nabisco".

Calculate the average of values in the Calories, Fiber, and Sugars columns for each manufacturer.

Find the maximum value in the Sugars column for each manufacturer.

Find the minimum value in the Fiber column for each manufacturer.

Extract the cereal with the lowest amount of grams of sugar per manufacturer in a new DataFrame.
"""
cereals = pd.read_csv('cereals.csv')
cereals_group_by_df = cereals.groupby('Manufacturer')

print('Total groups')
print(len(cereals_group_by_df))
print('#' * 80)
print('size per group')
print(cereals_group_by_df.size())
print('#' * 80)
print('cerials belonging to Nabisco')
print(cereals_group_by_df.get_group('Nabisco'))
print('#' * 80)
print('Average values per group')
print(cereals_group_by_df.mean())
print('#' * 80)
print('maximum value in the Sugars column for each manufacturer')
print(cereals_group_by_df['Sugars'].max())
print('#' * 80)
print(' minimum value in the Fiber column for each manufacturer')
print(cereals_group_by_df['Fiber'].min())


def get_largest_row(df):
    return df.nlargest(1, "Sugars")
print('#' * 80)

print(cereals_group_by_df.apply(get_largest_row))
