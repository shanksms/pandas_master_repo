import pandas as pd
"""
The nfl.csv file contains a list of players in the National Football League with similar Name, Team, Position, Birthday,
and Salary columns. See whether you can answer these questions:

1. How can we import the nfl.csv file? What’s an effective way to convert the values in its Birthday column to datetimes?

2. What are the two ways we can set the DataFrame index to store the player names?

3. How can we count the number of players per team in this data set?

4. Who are the five highest-paid players?

5. How can we sort the data set first by teams in alphabetical order and then by salary in descending order?

6. Who is the oldest player on the New York Jets roster, and what is his birthday?
"""

nfl_df = pd.read_csv('nfl.csv', parse_dates=['Birthday'])
print(nfl_df.dtypes)
print('setting name as index')
print(nfl_df.set_index('Name'))
print('#' * 50)
print('Count number of players per team')
print(nfl_df.loc[:, ['Team']].value_counts())
print('#' * 50)
print('Find top 5 players by salary')
print(nfl_df.nlargest(columns=['Salary'], n=5).loc[:, ['Name']])
print('#' * 50)
print('Sort by players name alphabetically and by salary in descending order')
print(nfl_df.sort_values(by=['Team', 'Salary'], ascending=[True, False]))
print('#' * 50)
print('Oldest player on the New York Jets roster. What is his birthday')

