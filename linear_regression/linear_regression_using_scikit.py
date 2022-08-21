import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('single_independent_variable_linear_small.csv')
X = df.loc[:, ['x']].to_numpy()
Y = df.loc[:, ['y']].to_numpy()
fit = LinearRegression().fit(X, Y)
m = fit.coef_.flatten()
b = fit.intercept_.flatten()
print("m = {0}".format(m))
print("b = {0}".format(b))

# show in chart
plt.plot(X, Y, 'o') # scatterplot
plt.plot(X, m*X+b) # line
plt.show()