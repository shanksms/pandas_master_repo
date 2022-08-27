import pandas as pd

points_df = pd.read_csv(r'single_independent_variable_linear_small.csv')


def using_pandas_library():
    x = points_df.loc[:, 'x']
    y = points_df.loc[:, 'y']
    print('Pearson corr {}'.format(x.corr(y)))


def from_scratch():
    pass


if __name__ == '__main__':
    using_pandas_library()