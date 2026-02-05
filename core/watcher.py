import asyncio
import logging

logger = logging.getLogger(__name__)

class PriceWatcher:
    def __init__(self, client, state, alert_manager, config):
        self.client = client
        self.state = state
        self.alerts = alert_manager
        self.symbols = config["symbols"]
        self.interval = config.get("check_interval_seconds", 10)
        
        tg_config = config.get("alerts", {}).get("telegram", {})
        self.tg_enabled = tg_config.get("enabled", False)
        self.chat_id = tg_config.get("chat_id")
    
    async def start(self):
        logger.info("PriceWatcher started (Async)...")
        while True:
            for item in self.symbols:
                symbol = item["symbol"]
                threshold = item["change_threshold_percent"]

                try:
                    price = await self.client.get_price(symbol)
                    prev_price = self.state.update(symbol, price)

                    if prev_price:
                        change = (price - prev_price) / prev_price * 100
                        if abs(change) >= threshold:
                            self.alerts.trigger(symbol, price, change)
                            
                            if self.tg_enabled and self.chat_id:
                                msg = (f"🚀 <b>Price Alert</b>\n\n"
                                       f"Pair: <code>{symbol}</code>\n"
                                       f"Price: <b>{price:.4f}</b>\n"
                                       f"Change: <b>{change:.2f}%</b>")
                                await self.alerts.notify_user(self.chat_id, msg)
                except Exception as e:
                    logger.error(f"Error in Watcher loop for {symbol}: {e}")

            await asyncio.sleep(self.interval)
