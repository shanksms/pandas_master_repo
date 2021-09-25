from pathlib import Path

import statsmodels.api as sm
import pandas as pd

def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

path = Path(__file__).parent / "../stock_px_2.csv"
close_px = pd.read_csv(path, index_col=0, parse_dates=True)
rets = close_px.pct_change().dropna()
rets['year'] = rets.index.year
by_year = rets.groupby(['year'])
print(by_year.apply(regress, 'AAPL', ['SPX']))