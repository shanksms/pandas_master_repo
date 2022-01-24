import pandas as pd


def correlation_example(df: pd.DataFrame):
    print(df)
    print(df.corr())




if __name__ == '__main__':
    df = pd.DataFrame(
        {
            'a': [1, 4, 3],
            'b': [2, 4, 6],
            'c': [5, 3, 4]
        }
    )
    correlation_example(df)