# BybitPriceAlertBot 🚀
BybitPriceAlertBot is a high-performance, asynchronous cryptocurrency price monitoring system built with Python. It tracks real-time price movements on the Bybit Spot market and delivers instant alerts via Telegram when predefined thresholds are met.

Built with a focus on concurrency and modularity, this tool is a perfect foundation for professional trading alert systems.

---

## 💼 Client-Oriented Overview
This project showcases my ability to develop:
- Asynchronous Python Systems: Handling multiple tasks (monitoring + bot) concurrently using asyncio.
- Telegram Bot Integration: Real-time user notifications via Telegram API.
- Secure Data Handling: Implementation of Environment Variables for sensitive data (API tokens).
- Clean Architecture: Decoupled logic for easy maintenance and scaling.

---

## 🧠 What This Tool Does

- Fetches real-time spot prices from **Bybit public API**
- Monitors price changes for selected trading pairs
- Triggers alerts when price movement exceeds a defined percentage
- Logs all alerts for further analysis

This system focuses on **monitoring and alerting**, not automated trading.

---

## ⚙️ Key Features
- Asynchronous Engine (asyncio) Uses non-blocking I/O to handle market monitoring and Telegram polling simultaneously.
- Instant Telegram Alerts Receive formatted notifications directly to your phone the moment a price threshold is crossed.
- Environment-Based Security Sensitive data like BOT_TOKEN is protected using .env files (industry standard).
- Flexible Monitoring Logic Configurable price change percentages and check intervals via config.json.
- Structured Logging Maintains a local CSV database of all triggered alerts for post-market analysis.

---

## 🧠 Tech Stack
- Core: Python 3.10+
- Asynchrony: asyncio
- Networking: httpx (Async HTTP requests)
- Telegram: aiogram 3.x (Modern Telegram Bot framework)
- Security: python-dotenv
- Data: JSON (Config) & CSV (Logs)

---

## 🛠 Installation

```bash
git clone https://github.com/VasylK27/CryptoPriceAlertBot.git
cd CryptoPriceAlertBot
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
Security Configuration:
- Rename .env.example to .env.
- Add your BOT_TOKEN (from @BotFather) and CHAT_ID.

---

## ▶️ Running the Application

```bash
python main.py
```
After launch:
    - Selected symbols are monitored continuously
    - Alerts are printed to the console
    - Alert events are saved to CSV
    - Configuration can be changed without modifying code

---

## 🔧 Configuration

All monitoring rules are defined in config.json, including:
    - Trading pairs
    - Price change thresholds
    - Check interval
    - Alert output settings

---

## 🧩 Architecture Notes
- **Separation of Concerns:** Watcher handles logic, BybitClient handles API, and Bot handles delivery.
- **Scalability:** Designed to easily add new exchanges (Binance, OKX) or notification channels (Discord, Email).
- **Performance:** Asynchronous httpx requests ensure the bot remains responsive even under heavy monitoring loads.

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only.
It does not provide financial advice or trading guarantees.

---

## 💬 Freelance Note

This project represents the type of crypto monitoring and alert systems I build for freelance clients.
Similar tools can be customized based on specific requirements.

---

## 📜 License

MIT License

---
