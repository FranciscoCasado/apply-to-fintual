"""
Stock has a "Price" method that receives a date and returns its price
"""
import datetime


class Stock:

    def __init__(self, name: str, base_price: float, rate: float):
        self.name = name
        self.base_price = base_price
        self.rate = rate

    def price(self, date: datetime.date) -> float:
        """
        just for funnier testing (?) purposes, lets say these
        stocks grow at a fixed compuound rate, with base_price 
        value specified at January 1st of 2021, 
        """
        days = (date - datetime.date(2021,1,1)).days
        
        price = self.base_price * (1 + self.rate) ** (days/365.0)
        return price
