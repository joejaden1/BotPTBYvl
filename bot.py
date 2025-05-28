from telegram.ext import Updater, CommandHandler
from db import init_db
from modules_binance_trade import trade
from config import TELEGRAM_TOKEN

def main():
   init_db()
   updater = Updater(TELEGRAM_TOKEN, use_context=True)
   dp = updater.dispatcher

   dp.add_handler(CommandHandler("trade", trade))
# يمكنك إضافة المزيد من الأوامر هنا

   updater.start_polling()
   updater.idle()

if __name__ == "__main__":
   main()
