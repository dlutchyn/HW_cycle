from structures.stock_adt import Stock
from modules.stock_plotting import StockPlotting


def plot_portfolio(stocks_values, start=None, end=None, invest_num=None):
    """Return a figure of a plot of portfolio"""
    s, e = start, end
    stocks = [Stock(item[0], item[1], s, e) for item in stocks_values]
    plotter = StockPlotting(stocks, 'Adj Close', s, e, invest_num)
    return plotter.plot_portfolio()


def plot_ratio_change(stocks_values, start=None, end=None, invest_num=None):
    """Return a figure of a plot of ratio change"""
    s, e = start, end
    stocks = [Stock(item[0], item[1], s, e) for item in stocks_values]
    plotter = StockPlotting(stocks, 'Adj Close', s, e, invest_num)
    return plotter.plot_ratio()


# print(date_start)