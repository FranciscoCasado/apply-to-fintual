import unittest
import datetime

from ..portfolio import Portfolio
from .factories import PortfolioFactory


class TestPortfolio(unittest.TestCase):
    def test_cool_portfolio(self):
        p = PortfolioFactory.create("cool_portfolio")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        one_year_profit = ((1.07) * 200 + (1.2) * 100) / 300.0 - 1
        mid_year_profit = (
            (1.07) ** (181.0 / 365.0) * 200 + (1.2) ** (181.0 / 365.0) * 100
        ) / 300.0 - 1
        mid_year_annualized = (1 + mid_year_profit) ** (365 / 181.0) - 1

        self.assertEqual(p.profit(date1, date2, annualized=False), one_year_profit)
        self.assertEqual(p.profit(date1, date2, annualized=True), one_year_profit)

        self.assertEqual(p.profit(date1, mid_year, annualized=False), mid_year_profit)
        self.assertEqual(
            p.profit(date1, mid_year, annualized=True), mid_year_annualized
        )

    def test_zero_growth_portfolio(self):
        p = PortfolioFactory.create("zero_growth")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        one_year_profit = 0
        mid_year_profit = 0
        mid_year_annualized = 0

        self.assertEqual(p.profit(date1, date2, annualized=False), one_year_profit)
        self.assertEqual(p.profit(date1, date2, annualized=True), one_year_profit)

        self.assertEqual(p.profit(date1, mid_year, annualized=False), mid_year_profit)
        self.assertEqual(
            p.profit(date1, mid_year, annualized=True), mid_year_annualized
        )

    def test_terrible_portfolio(self):
        p = PortfolioFactory.create("terrible_portfolio")
        date1 = datetime.date(2021, 1, 1)
        mid_year = datetime.date(2021, 7, 1)  # 182nd day of year, except on leap years
        date2 = datetime.date(2022, 1, 1)

        one_year_profit = ((0.8) * 1000 + (1) * 500) / 1500 - 1
        mid_year_profit = ((0.8) ** (181.0 / 365.0) * 1000 + (1) * 500) / 1500 - 1
        mid_year_annualized = (1 + mid_year_profit) ** (365 / 181.0) - 1

        self.assertEqual(p.profit(date1, date2, annualized=False), one_year_profit)
        self.assertEqual(p.profit(date1, date2, annualized=True), one_year_profit)

        self.assertAlmostEqual(
            p.profit(date1, mid_year, annualized=False), mid_year_profit
        )
        self.assertAlmostEqual(
            p.profit(date1, mid_year, annualized=True), mid_year_annualized
        )
