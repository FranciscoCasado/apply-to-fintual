import unittest
import datetime

from ..stock import Stock
from .factories import StockFactory


class TestStock(unittest.TestCase):
    def test_zero_growth_stock(self):
        s = Stock("steady_inc")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)
        
        s.set_price_at_date(date1, 1000.0)
        s.set_price_at_date(date2, 1000.0)

        self.assertEqual(s.name, "steady_inc")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1000.0)
        
    def test_little_growth_stock(self):
        s = Stock("chillin_co")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)
        
        s.set_price_at_date(date1, 1000.0)
        s.set_price_at_date(date2, 1010.0)

        self.assertEqual(s.name, "chillin_co")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1010.0)
        
class TestStockFactory(unittest.TestCase):
    def test_piggy_bank(self):
        s = StockFactory.create("piggy_bank")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)
        
        self.assertEqual(s.name, "piggy_bank")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1000.0)
    
    def test_stark_industries(self):
        s = StockFactory.create("stark_industries")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1) # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)
        
        self.assertEqual(s.name, "stark_industries")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(mid_year), 1000.0 * (1.2)** (181.0/365.0))
        self.assertEqual(s.price(date2), 1200.0)