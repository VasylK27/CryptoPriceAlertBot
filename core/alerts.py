import csv
from datetime import datetime, timezone
from pathlib import Path

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

        print(
            f"[ALERT] {symbol} | price={price:.2f} | change={change_percent:.2f}%"
        )

        with open(self.csv_path, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, symbol, price, change_percent])
