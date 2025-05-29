from flask import Flask, request
from telegram.ext import Dispatcher, CommandHandler
from telegram import Bot, Update
from config import TELEGRAM_TOKEN
from binance_trade import trade
from db import init_db

app = Flask(__name__)
bot = Bot(token=TELEGRAM_TOKEN)


dispatcher = Dispatcher(bot, None, workers=0, use_context=True)


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

@app.route(f"/{TELEGRAM_TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "OK", 200


@app.before_first_request
def setup_webhook():
    init_db()  
    app_url = f"https://botptbyvl.onrender.com/{TELEGRAM_TOKEN}"  
    bot.delete_webhook()  
    bot.set_webhook(url=app_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
