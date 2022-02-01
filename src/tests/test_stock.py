import unittest
import datetime

from ..stock import Stock


class TestStock(unittest.TestCase):
    def test_zero_growth_stock(self):
        s = Stock("stuck_brothers")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)

        s.set_price_at_date(date1, 1000.0)
        s.set_price_at_date(date2, 1000.0)

        self.assertEqual(s.name, "stuck_brothers")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1000.0)

    def test_little_growth_stock(self):
        s = Stock("shy_ltd")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)

        s.set_price_at_date(date1, 1000.0)
        s.set_price_at_date(date2, 1020.0)

        self.assertEqual(s.name, "shy_ltd")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1020.0)
