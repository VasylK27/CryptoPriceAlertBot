import requests

class BybitClient:
    BASE_URL = "https://api.bybit.com/v5/market/tickers"

    def get_price(self, symbol: str) -> float:
        params = {
            "category": "spot",
            "symbol": symbol
        }
        response = requests.get(self.BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        data =response.json()

        return float(data["result"]["list"][0]["lastPrice"])
