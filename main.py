import json
import logging

from core.watcher import PriceWatcher
from core.state import PriceState
from core.alerts import AlertManager
from services.bybit_client import BybitClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

logger = logging.getLogger(__name__)


def load_config():
    with open("config.json", "r") as f:
        return json.load(f)


def main():
    logger.info("The app started.")
    
    config = load_config()

    client = BybitClient()
    state = PriceState()
    alerts = AlertManager()

    watcher = PriceWatcher(client, state, alerts, config)
    watcher.start()


if __name__ == "__main__":
    main()
