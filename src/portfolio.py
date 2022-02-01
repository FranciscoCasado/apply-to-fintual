"""
**simple** Portfolio class that has a collection of Stocks and
a "profit" method that receives 2 dates and returns the profit 
of the Portfolio between those dates.
"""
from .stock import Stock


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = dict()
        self.stock_units = dict()

    def add_stock(self, stock: Stock, units: float):
        if stock.name not in self.stocks:
            self.stocks[stock.name] = stock
            self.stock_units[stock.name] = 0

        self.stock_units[stock.name] += units

    def profit(self, date1, date2, annualized=True) -> float:
        if not self.stock_units:
            return 0

        value_at_date1 = 0
        value_at_date2 = 0
        for name, stock in self.stocks.items():
            value_at_date1 += stock.price(date1) * self.stock_units[name]
            value_at_date2 += stock.price(date2) * self.stock_units[name]

        profit = (value_at_date2 / value_at_date1) - 1

        if annualized:
            days = date2.day - date1.day
            profit = (1 + profit) ** (365 / days) - 1

        return profit
