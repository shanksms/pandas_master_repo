import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



df = pd.read_csv('single_independent_variable_linear_small.csv')
# Test with a given line
m = 1.93939
b = 4.73333

def print_residuals(row):
    y_actual = row['y']
    y_predit = m*row['x'] + b
    residual = y_actual - y_predit
    print(residual)


df.apply(print_residuals, axis=1)

