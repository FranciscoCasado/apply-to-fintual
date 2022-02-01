"""
Stock has a "Price" method that receives a date and returns its price
"""
import datetime
from datetime import date as Date


class Stock:
    def __init__(self, name: str):
        self.name = name
        self.prices = dict()

    def set_price_at_date(self, date: Date, value: float):
        self.prices[date] = value

    def price(self, date: Date) -> float:
        if date not in self.prices:
            raise ValueError(f"No information for the specified date: {date}")
        return self.prices[date]
