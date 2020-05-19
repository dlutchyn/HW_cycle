import os
import pandas as pd
import yfinance as yf


def get_names_from_data(filename):
    """Get the data(name and symbol of the stock at the market)
    from the filename"""
    stocks_data = []
    data = pd.read_csv(os.path.join(os.getcwd(), filename), sep='\t', engine='python')
    for symbol, name in zip(data['Symbol'], data['Name']):
        stocks_data.append((name, symbol))
    return stocks_data[:10]


if __name__ == "__main__":
    start, end = '2020-1-1', '2020-2-2'
    stocks_data = get_names_from_data('../sources/crypto_currency.csv')
    delet = []
    for elem in stocks_data:
        a = yf.download(elem[1], start=start, end=end)
        if a.empty:
            delet.append(elem[0])
    print(delet)
