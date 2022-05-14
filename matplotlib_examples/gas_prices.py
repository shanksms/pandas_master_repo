import matplotlib.pyplot as plt
import pandas as pd


class GasPrice:
    def __init__(self):
        self.gas_price_df = pd.read_csv('gas_prices.csv')

    def get_gas_price_df(self):
        return self.gas_price_df


def line_graph(gas_price_df: pd.DataFrame):
    plt.title('Gas Prices over time in USD')
    #plt.figure(figsize=(8, 5))
    plt.plot(gas_price_df['Year'], gas_price_df['USA'], 'b.-', label='USA')
    plt.plot(gas_price_df['Year'], gas_price_df['Canada'], 'r.-' , label='Canada')
    plt.xticks(gas_price_df['Year'][::3])
    plt.xlabel('Year')
    plt.ylabel('USD')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    gas_price_df = GasPrice().get_gas_price_df()
    line_graph(gas_price_df)