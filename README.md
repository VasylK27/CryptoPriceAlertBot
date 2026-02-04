# BybitPriceAlertBot 🚀

**BybitPriceAlertBot** is a real-time cryptocurrency price monitoring and alert system built in **Python**.
It tracks price changes on the **Bybit Spot market** and triggers alerts when predefined thresholds are exceeded.

The project is designed as a **lightweight, extendable monitoring tool** for traders, analysts, and crypto-related businesses.

---

## 💼 Client-Oriented Overview

This project demonstrates how I build:
- Real-time crypto price monitoring systems
- Custom alert engines for exchanges
- Configurable data collection tools
- Clean and extendable Python architectures

Typical client use cases:
- Price movement alerts
- Market monitoring dashboards
- Research and analytics tools
- Integration with trading or notification systems

---

## 🧠 What This Tool Does

- Fetches real-time spot prices from **Bybit public API**
- Monitors price changes for selected trading pairs
- Triggers alerts when price movement exceeds a defined percentage
- Logs all alerts for further analysis

This system focuses on **monitoring and alerting**, not automated trading.

---

## ⚙️ Key Features

- **Exchange-Agnostic Architecture**  
  Designed to be easily extended to other exchanges (Binance, OKX, Kraken).

- **Configurable Alert Rules**  
  All symbols and thresholds are defined via `config.json`.

- **Low-Latency Monitoring**  
  Uses public REST API endpoints with minimal overhead.

- **CSV-Based Logging**  
  All alerts are stored locally for later analysis.

- **Clean Project Structure**  
  Business logic, exchange services, and configuration are clearly separated.

---

## 🛠 Tech Stack

- Python
- REST APIs (Bybit public endpoints)
- Requests
- JSON-based configuration
- CSV data logging

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

- Clear separation between:
    - exchange API services
    - monitoring logic
    - alert handling
- Designed for easy extension:
    - Telegram / Email alerts
    - WebSocket price streams
    - Futures markets
    - Multi-exchange support

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
