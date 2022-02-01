import unittest
import datetime

from ..stock import Stock


class TestStock(unittest.TestCase):
    def test_zero_growth_stock(self):
        s = Stock("rocket", base_price=10, rate=0)
        date = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "rocket")
        self.assertEqual(s.price(date), 10)

    def test_little_growth_stock(self):
        s = Stock("rocket", base_price=10, rate=0.01)
        date = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "rocket")
        self.assertAlmostEqual(s.price(date), 10.1)

    def test_little_growth_stock_before_2021(self):
        s = Stock("rocket", base_price=10, rate=0.01)
        date = datetime.date(2020, 12, 1)

        self.assertEqual(s.name, "rocket")
        self.assertAlmostEqual(s.price(date), 10 * (1 - 0.01) ** (30 / 365), places=3)
