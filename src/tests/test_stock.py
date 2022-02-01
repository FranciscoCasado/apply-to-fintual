import unittest
import datetime

from ..stock import Stock


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