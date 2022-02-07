import pandas as pd

neighborhoods = pd.read_csv(
    "neighborhoods.csv",
    index_col=[0, 1, 2],
    header=[0, 1]
)

print(neighborhoods.head())
print(neighborhoods.info())
print('#' * 80)
print('row indexes')
print(neighborhoods.index)
print('#' * 80)
print('column indexes')
print(neighborhoods.columns)
print('#' * 80)
print('Level values')
print(neighborhoods.index.get_level_values(1))
print(neighborhoods.index.get_level_values("City"))
# Since column indexes have no names, let us assign them name
neighborhoods.columns.names = ["Category", "Subcategory"]
print(neighborhoods.head(3))
print('#' * 80)
print('column level values')
print(neighborhoods.columns.get_level_values(0))
print(neighborhoods.columns.get_level_values("Category"))
print(neighborhoods.nunique())

