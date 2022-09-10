import pandas as pd
import matplotlib.pyplot as plt

'''
https://raw.githubusercontent.com/DataForScience/Timeseries/master/data/CDC.csv
'''

def gdp_data():
    # GDP.csv contains US quarterly GDP data for past 70 years
    GDP = pd.read_csv('GDP.csv', parse_dates=['DATE'])
    GDP = GDP.set_index('DATE')
    ax = GDP.plot(legend=False)
    ax.set_ylabel(r'GDP ($\$B$)')
    plt.show()


def cdc_data():
    ILI = pd.read_csv('CDC.csv')


if __name__ == '__main__':
    gdp_data()