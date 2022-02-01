from ..portfolio import Portfolio
from ..stock import Stock


class PortfolioFactory:
    def create_portfolio(name):
        portfolio = Portfolio(name)
        
        if name == "nice_candidate":
            portfolio_composition = [
                [Stock("fintual", base_price=53.0, rate=0.1), 100],
                [Stock("platanus", base_price=22.0, rate=0.1), 100],
                [Stock("cornershop", base_price=17.0, rate=0.1), 100],
                [Stock("notco", base_price=16.0, rate=0.1), 100],
            ]
            for [stock, units] in portfolio_composition:
                portfolio.add_stock(stock, units)
                
        if name == "zero_growth":
            portfolio_composition = [
                [Stock("stuck_ltd", base_price=100.0, rate=0.0), 100],
                [Stock("stalled_co", base_price=100.0, rate=0.0), 100]
            ]
            for [stock, units] in portfolio_composition:
                portfolio.add_stock(stock, units)
        
        return portfolio
