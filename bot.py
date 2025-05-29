from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from binance_trade import trade
from db import init_db

def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت التداول. استخدم الأمر /trade لتنفيذ صفقة.")

def trade_handler(update, context):
    # call your trading logic here, adapt if needed
    trade()
    update.message.reply_text("تم تنفيذ الصفقة!")

def main():
    init_db()  # initialize database connection

    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trade", trade_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
