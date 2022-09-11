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
    ILI = ILI.loc[:, ['Percent of Deaths Due to Pneumonia and Influenza', 'Expected', 'Threshold']]
    ax = ILI.plot()
    plt.show()

def sun_activity_data():
    sun_activity = pd.read_csv('sun.csv')
    ax = sun_activity.plot(x='YEAR', y='SUNACTIVITY', legend=False)
    ax.set_xlabel('Year')
    ax.set_ylabel('Sun spot activity')
    plt.show()


def djia_data():
    djia = pd.read_csv('DJIA.csv', parse_dates=['DATE'], na_values='.')
    ax = djia.plot(x='DATE', y='DJIA')
    plt.show()


def airline_data():
    airline = pd.read_csv('international-airline-passengers.csv', parse_dates=['Month'], sep=';')
    airline = airline.set_index('Month')
    ax = airline.plot(legend=False)
    ax.set_xlabel('Date')
    ax.set_ylabel('Passengers')
    plt.show()



if __name__ == '__main__':
    airline_data()