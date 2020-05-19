import pandas as pd
import yfinance as yf
import numpy as np


class Stock:
    """Represent a STOCK ADT using pandas DataFrame as a main structure"""
    def __init__(self, stock_name, stock_symbol=None, start=None, end=None):
        """Initialize the stock"""
        self.name = stock_name
        self._data = pd.DataFrame()
        self.symbol = stock_symbol
        if not stock_symbol:
            self.symbol = self.name
        self.start, self.end = start, end
        self.process_yf()
        self._ratio_change = None
        self.profit = None

    def process_yf(self):
        """Process yahoo finance api to get data"""
        self._data = yf.download(self.symbol, start=self.start, end=self.end)

    def calculate_change_ratio(self):
        """Calculate the logarithmic change ratio of stock data"""
        s_change_ratio_data = self._data.apply(lambda x: np.log(x) - np.log(x.shift(1)))
        self._ratio_change = s_change_ratio_data
        return s_change_ratio_data

    def calculate_growth(self, column_name):
        """Calculate ratio growth of the stock"""
        if not self._ratio_change:
            self.calculate_change_ratio()
        self.profit = self._ratio_change[column_name].sum()
        return self.profit


