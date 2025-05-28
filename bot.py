from telegram.ext import Updater, CommandHandler
from config import TELEGRAM_TOKEN
from modules.binance_trade import trade

def start(update, context):
    update.message.reply_text("مرحبًا! أنا بوت التداول. استخدم الأمر /trade لتنفيذ صفقة.")
from db import init_db
init_db()
def main():
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("trade", trade))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
