import datetime

from ..portfolio import Portfolio
from ..stock import Stock


class StockFactory:

    companies = {
        "stalled_co": {"base_price": 1000.0, "rate": 0.0},
        "piggy_bank": {"base_price": 1000.0, "rate": 0.0},
        "steady_inc": {"base_price": 1000.0, "rate": 3.5},
        "chillin_ltd": {"base_price": 1000.0, "rate": 7.0},
        "stark_industries": {"base_price": 1000.0, "rate": 20.0},
        "block_buster": {"base_price": 1000.0, "rate": -20.0},
    }

    def create(name: str):
        if name not in __class__.companies:
            raise ValueError("name of the company is not registered")

        stock = Stock(name)

        base_price = __class__.companies[name]["base_price"]
        rate = __class__.companies[name]["rate"]

        start_date = datetime.date(2021, 1, 1)
        for days in range(366):
            date = start_date + datetime.timedelta(days=days)
            value = base_price * (1 + rate/100.0) ** (days / 365.0)
            stock.set_price_at_date(date, value)

        return stock


class PortfolioFactory:
    def create(name):
        portfolio = Portfolio(name)

        if name == "cool_portfolio":
            chillin_ltd = StockFactory.create("chillin_ltd")
            stark_industries = StockFactory.create("stark_industries")
            
            portfolio.add_stocks(chillin_ltd, 100)
            portfolio.add_stocks(stark_industries, 100)

        elif name == "zero_growth":
            stalled_co = StockFactory.create("stalled_co")
            piggy_bank = StockFactory.create("piggy_bank")
            
            portfolio.add_stocks(stalled_co, 100)
            portfolio.add_stocks(piggy_bank, 100)
        
        elif name == "terrible_portfolio":
            piggy_bank = StockFactory.create("piggy_bank")
            block_buster = StockFactory.create("block_buster")
            
            portfolio.add_stocks(piggy_bank, 100)
            portfolio.add_stocks(block_buster, 100)
            

        return portfolio
