import pandas as pd
"""
We have two data sets for you to play with. The used_cars.csv file is a listing of used cars for sale on the classifieds website Craigslist. Each row includes the car’s manufacturer, year of production, fuel type, transmission type, and price:

In  [33] cars = pd.read_csv("used_cars.csv")
         cars.head()
 
Out [33]
 
  Manufacturer  Year Fuel Transmission  Price
0        Acura  2012  Gas    Automatic  10299
1       Jaguar  2011  Gas    Automatic   9500
2        Honda  2004  Gas    Automatic   3995
3    Chevrolet  2016  Gas    Automatic  41988
4          Kia  2015  Gas    Automatic  12995
The minimum_wage.csv data set is a collection of minimum wages across the United States. The data set has a State column and multiple year columns:

In  [34] min_wage = pd.read_csv("minimum_wage.csv")
         min_wage.head()
 
Out [34]
 
        State  2010  2011  2012  2013  2014  2015   2016   2017
0     Alabama  0.00  0.00  0.00  0.00  0.00  0.00   0.00   0.00
1      Alaska  8.90  8.63  8.45  8.33  8.20  9.24  10.17  10.01
2     Arizona  8.33  8.18  8.34  8.38  8.36  8.50   8.40  10.22
3    Arkansas  7.18  6.96  6.82  6.72  6.61  7.92   8.35   8.68
4  California  9.19  8.91  8.72  8.60  9.52  9.51  10.43  10.22
Here are the challenges:

1. Aggregate the sum of car prices in cars. Group the results by fuel type on the row axis.

2. Aggregate the count of cars in cars. Group the results by manufacturer on the index axis and transmission type on the column axis. Show the subtotals for both the rows and columns.

3. Aggregate the average of car prices in cars. Group the results by year and fuel type on the index axis and transmission type on the column axis.

4. Given a DataFrame from the preceding challenge, move the transmission level from the column axis to the row axis.

5. Convert the min_wage from wide format to narrow format. In other words, move the data from the eight year columns (2010–17) to a single column.
"""
used_car_df = pd.read_csv('used_cars.csv')
print(used_car_df.pivot_table(index='Fuel', values='Price', aggfunc='sum'))
print('#' * 80)
print(used_car_df.pivot_table(index='Manufacturer', columns='Transmission', values='Price', aggfunc='count', margins=True))
print('#' * 80)
print(used_car_df.pivot_table(index=['Year', 'Fuel'], columns=['Transmission'], values='Price', aggfunc='mean'))
print('#' * 80)
agg_df = used_car_df.pivot_table(index=['Year', 'Fuel'], columns=['Transmission'], values='Price', aggfunc='mean')
print(agg_df.stack())
print('#' * 80)
min_wage_df = pd.read_csv('minimum_wage.csv')
print(min_wage_df.head())
print('#' * 80)

year_columns = [
    "2010", "2011", "2012", "2013",
    "2014", "2015", "2016", "2017"
]

min_wage_df.melt(id_vars="State", value_vars=year_columns)

