import csv
from datetime import datetime, timezone
from pathlib import Path
from bot.instance import bot
from aiogram.enums import ParseMode

class AlertManager:
    def __init__(self, csv_path: str = "data/alerts.csv"):
        self.csv_path = Path(csv_path)
        self.csv_path.parent.mkdir(exist_ok=True)
        if not self.csv_path.exists():
            with open(self.csv_path, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "symbol", "price", "change_percent"])
        
    def trigger(self, symbol: str, price: float, change_percent: float):
        timestamp = datetime.now(timezone.utc).isoformat()
        print(f"[ALERT] {symbol} | price={price:.2f} | change={change_percent:.2f}%")
        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, symbol, price, change_percent])

    async def notify_user(self, chat_id: int, message: str):
        try:
            await bot.send_message(chat_id=chat_id, text=message, parse_mode=ParseMode.HTML)
        except Exception as e:
            print(f"Failed to send Telegram message: {e}")