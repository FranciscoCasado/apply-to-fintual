"""
**simple** Portfolio class that has a collection of Stocks and
a "profit" method that receives 2 dates and returns the profit 
of the Portfolio between those dates.
"""
import datetime
from datetime import date as Date


from .stock import Stock


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = dict()
        self.stock_units = dict()

    def add_stocks(self, stock: Stock, units: float) -> float:
        if stock.name not in self.stocks:
            self.stocks[stock.name] = stock
            self.stock_units[stock.name] = 0

        self.stock_units[stock.name] += units
        return self.stock_units[stock.name]

    def profit(self, date1, date2, annualized=True) -> float:
        if date1 >= date2:
            raise ValueError(
                f"date2 ({date2}) must be greater (>) than date1 ({date1})"
            )

        if annualized:
            return self.annualized_return(date1, date2)
        return self.cumulative_return(date1, date2)

    def cumulative_return(self, date1, date2) -> float:
        if not self.stock_units:
            return 0

        value_at_date1 = 0
        value_at_date2 = 0
        for name, stock in self.stocks.items():
            value_at_date1 += stock.price(date1) * self.stock_units[name]
            value_at_date2 += stock.price(date2) * self.stock_units[name]

        return (value_at_date2 / value_at_date1) - 1

    def annualized_return(self, date1, date2) -> float:
        rate = self.cumulative_return(date1, date2)
        days_held = (date2 - date1).days

        return (1 + rate) ** (365.0 / days_held) - 1
