from pathlib import Path

import pandas as pd


path = Path(__file__).parent / "../stock_px_2.csv"
close_px = pd.read_csv(path, index_col=0, parse_dates=True)
print(close_px.info())
print(close_px[-4:])
print('#' * 70)
rets = close_px.pct_change().dropna()
print(rets)
print('#' * 70)
get_year = lambda x : x.year
rets['year'] = rets.index.year
print(rets)
print('#' * 70)
by_year = rets.groupby(['year'])
result = by_year.apply(lambda x : x.corrwith(x['SPX'])).drop(columns=['year'])
print(result)