class PriceState:
    def __init__(self):
        self.last_prices = {}

    def update(self, symbol: str, price: float):
        previous = self.last_prices.get(symbol)
        self.last_prices[symbol] = price
        return previous
