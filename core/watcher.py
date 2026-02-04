import time

class PriceWatcher:
    def __init__(self, client, state, alert_manager, config):
        self.client = client
        self.state = state
        self.alerts = alert_manager
        self.symbols = config["symbols"]
        self.interval = config.get("check_interval_seconds", 10)
    
    def start(self):
        while True:
            for item in self.symbols:
                symbol = item["symbol"]
                threshold = item["change_threshold_percent"]

                price = self.client.get_price(symbol)
                prev_price = self.state.update(symbol, price)

                if prev_price:
                    change = (price - prev_price) / prev_price * 100
                    if abs(change) >= threshold:
                        self.alerts.trigger(symbol, price, change)

            time.sleep(self.interval)
