import unittest
import datetime

from .factories import Portfolio, PortfolioFactory, Stock, StockFactory


class TestStockFactory(unittest.TestCase):
    def test_company_not_registered(self):
        self.assertRaises(ValueError, StockFactory.create, "non_existent_company")

    def test_piggy_bank(self):
        s = StockFactory.create("piggy_bank")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "piggy_bank")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1000.0)

    def test_stalled_co(self):
        s = StockFactory.create("stalled_ltd")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "stalled_ltd")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(date2), 1000.0)

    def test_chillin_ltd(self):
        s = StockFactory.create("chillin_co")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "chillin_co")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(mid_year), 1000.0 * (1.07) ** (181.0 / 365.0))
        self.assertEqual(s.price(date2), 1070.0)

    def test_stark_industries(self):
        s = StockFactory.create("stark_industries")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "stark_industries")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(mid_year), 1000.0 * (1.2) ** (181.0 / 365.0))
        self.assertEqual(s.price(date2), 1200.0)

    def test_block_buster(self):
        s = StockFactory.create("block_buster")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        self.assertEqual(s.name, "block_buster")
        self.assertEqual(s.price(date1), 1000.0)
        self.assertEqual(s.price(mid_year), 1000.0 * (0.8) ** (181.0 / 365.0))
        self.assertEqual(s.price(date2), 800.0)


class TestPortfolioFactory(unittest.TestCase):
    def test_empty_portfolio(self):
        p = PortfolioFactory.create("empty")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2021, 1, 2)

        self.assertEqual(p.name, "empty")
        self.assertEqual(p.profit(date1, date2), 0)
        self.assertRaises(ValueError, p.profit, date2, date1)

    def test_create_cool_portfolio(self):
        p = PortfolioFactory.create("cool_portfolio")

        self.assertEqual(p.name, "cool_portfolio")
        self.assertEqual(set(p.stocks.keys()), set(["chillin_co", "stark_industries"]))
        self.assertEqual(p.stock_units["chillin_co"], 200)
        self.assertEqual(p.stock_units["stark_industries"], 100)

    def test_create_terrible_portfolio(self):
        p = PortfolioFactory.create("terrible_portfolio")

        self.assertEqual(p.name, "terrible_portfolio")
        self.assertEqual(set(p.stocks.keys()), set(["piggy_bank", "block_buster"]))
        self.assertEqual(p.stock_units["piggy_bank"], 500)
        self.assertEqual(p.stock_units["block_buster"], 1000)

    def test_create_zero_growth(self):
        p = PortfolioFactory.create("zero_growth")

        self.assertEqual(p.name, "zero_growth")
        self.assertEqual(set(p.stocks.keys()), set(["stalled_ltd", "piggy_bank"]))
        self.assertEqual(p.stock_units["stalled_ltd"], 300)
        self.assertEqual(p.stock_units["piggy_bank"], 200)

    def test_zero_growth_portfolio_invalid_dates(self):
        p = PortfolioFactory.create("zero_growth")
        date1 = datetime.date(2021, 1, 1)
        date2 = datetime.date(2021, 7, 1)
        date3 = datetime.date(2022, 1, 1)
        date4 = datetime.date(2022, 1, 31)

        self.assertEqual(p.profit(date1, date2), 0)
        self.assertEqual(p.profit(date1, date3), 0)
        self.assertRaises(ValueError, p.profit, date1, date4)
        self.assertRaises(ValueError, p.profit, date2, date1)
