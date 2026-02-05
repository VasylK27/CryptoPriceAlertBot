import os
from dotenv import load_dotenv
import asyncio
import json
import logging
from bot.instance import bot, dp
from core.watcher import PriceWatcher
from core.state import PriceState
from core.alerts import AlertManager
from services.bybit_client import BybitClient

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

async def main():
    logger.info("Application is starting...")
    config = load_config()

    if not config["alerts"]["telegram"].get("chat_id"):
        config["alerts"]["telegram"]["chat_id"] = os.getenv("CHAT_ID")

    client = BybitClient()
    state = PriceState()
    alerts = AlertManager()
    watcher = PriceWatcher(client, state, alerts, config)

    await asyncio.gather(
        dp.start_polling(bot),
        watcher.start()
    )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application stopped by user.")
