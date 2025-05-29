from flask import Flask, request
from telegram.ext import Dispatcher, CommandHandler
from telegram import Bot, Update
from config import TELEGRAM_TOKEN
from binance_trade import trade
from db import init_db

app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)

# Dispatcher
dispatcher = Dispatcher(bot, None, workers=4, use_context=True)

# Command Handlers
def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت التداول. استخدم الأمر /trade لتنفيذ صفقة.")

def trade_handler(update, context):
    try:
        trade()
        update.message.reply_text("تم تنفيذ الصفقة!")
    except Exception as e:
        update.message.reply_text(f"حدث خطأ أثناء تنفيذ الصفقة: {e}")

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("trade", trade_handler))

# Webhook route
@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200

# ✅ Safe manual webhook setup
@app.route("/set_webhook", methods=["GET"])
def set_webhook():
    init_db()
    webhook_url = f"https://{request.host}/{TELEGRAM_TOKEN}"
    success = bot.set_webhook(url=webhook_url)
    return f"Webhook set: {success}"

# Run locally (for testing)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
