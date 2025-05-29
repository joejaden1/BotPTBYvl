import os

BINANCE_API_KEY = ("BINANCE_API_KEY")
BINANCE_API_SECRET = ("BINANCE_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TELEGRAM_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set!")

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
