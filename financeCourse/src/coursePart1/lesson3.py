'''
Created on 15.11.2017

@author: sabrinahiestand
'''
import pandas as pd
import numpy as np
import symbol
import os
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from pandas.core.indexes.datetimes import date_range
import datetime as dt
def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    #===========================================================================
    # 
    #===========================================================================
    
    #print (df)
    
    
    print (df)
    print(normalize_data(df))
    
    
    plot_data(normalize_data(df.ix[start_index:end_index,columns]), title="")
    
            

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_symbol_from_google(symbol):
    goog = web.DataReader(symbol, data_source='google', start="2010-01-01", end="2017-11-15")
    print(goog)
    #goog = web.DataReader(symbol,data_source='google', start )

def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    print (df)
    return df


def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def normalize_data(df):
    
    return df/df.ix[0,:]


def test_run():
    # Define a date range


    dates = pd.date_range('2013-01-01', '2013-12-31')
    
    # Choose stock symbols to read
    symbols = ['AAPL', 'IBM','SPY']  # SPY will be added in d()
    
    # Get stock data
    df = get_data(symbols, dates)
    
    # Slice and plot
    plot_selected(df, symbols, '2013-01-01', '2013-12-31')


if __name__ == "__main__":
    test_run()
