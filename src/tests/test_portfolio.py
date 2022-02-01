import unittest
from datetime import date

from ..portfolio import Portfolio
from .portfolio_factory import PortfolioFactory


class TestPortfolio(unittest.TestCase):
    def test_empty_portfolio(self):
        p = PortfolioFactory.create_portfolio("empty")
        date1 = date(2022, 1, 1)
        date2 = date(2022, 1, 2)

        self.assertEqual(p.name, "empty")
        self.assertEqual(p.profit(date1, date2), 0)

    def test_zero_growth_portfolio(self):
        p = PortfolioFactory.create_portfolio("zero_growth")
        date1 = date(2022, 1, 1)
        date2 = date(2022, 1, 31)

        expected_profit = 0  # price did not go up or down

        self.assertEqual(p.name, "zero_growth")
        self.assertEqual(p.profit(date1, date2), expected_profit)

    def test_nice_candidate_portfolio_1(self):
        p = PortfolioFactory.create_portfolio("nice_candidate")
        date1 = date(2022, 1, 1)
        date2 = date(2022, 1, 31)

        expected_profit = 0.1  # this portfolio has 0.1 annual growth rate

        self.assertEqual(p.name, "nice_candidate")
        self.assertAlmostEqual(p.profit(date1, date2), expected_profit)

    def test_nice_candidate_portfolio_3(self):
        p = PortfolioFactory.create_portfolio("nice_candidate")
        date1 = date(2021, 1, 1)
        date2 = date(2022, 1, 31)

        expected_profit = 0.1  # this portfolio has 0.1 annual growth rate

        self.assertEqual(p.name, "nice_candidate")
        self.assertAlmostEqual(p.profit(date1, date2), expected_profit)
