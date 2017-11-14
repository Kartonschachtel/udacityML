'''
Created on 03.11.2017

@author: Ich
'''

import pandas as pd
import numpy as np
import symbol
import os
import matplotlib.pyplot as plt



def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    #dates=pd.date_range('2017-07-01', '2017-11-04')
    df1=pd.DataFrame(index=dates)
    
    for symbol in symbols:
        # TODO: Read and join data for each symbol
        print(symbol_to_path(symbol, 'data/'))
        df = pd.read_csv(symbol_to_path(symbol, 'data/'), index_col="Date",
                         parse_dates=True, usecols=['Date','Adj Close'],
                         na_values=['nan'])
        df = df.rename(columns={'Adj Close': symbol})
        
        df1=df1.join(df,how='inner')
        
    return df1


def test_run():
    
    # Define a date range
    dates = pd.date_range('2014-01-22', '2014-02-26')

    # Choose stock symbols to read
    symbols = ['AAPL', 'GOLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    #Slice by row_range
    print (df.ix['2014-01-01':'2014-01-31',['GOLD']])

     #print (df['GOLD'])
    #draw plot
#     df.plot()
#     plt.show()
    


if __name__ == "__main__":
    test_run()
