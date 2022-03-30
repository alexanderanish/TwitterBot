from re import T
import yfinance as yf
import numpy as np
from pandas_datareader import data



def marketCap(Tickers):
    marketCapData={}
    for str in Tickers:
        tickers = [(str.upper())]
        #print(tickers)
        try:
            market_cap=int(data.get_quote_yahoo(str)['marketCap'])
        except:
            print("Something wrong with "+str+". Set market cap to 0 for manual override")
            market_cap=0

        marketCapData[str.upper()]=market_cap
        #print(market_cap)
    output=dict(sorted(marketCapData.items(), key=lambda x: x[1], reverse=True))
    return output

if __name__ == '__main__':
    Tickers=["AAPL","GOOG","RY","HPQ"]

    print(Tickers)

    test=marketCap(Tickers)
    print(test)

    #x = market_cap=int(data.get_quote_yahoo("ARKK")['marketCap'])