from binance.client import Client
from telegram import Update
from telegram.ext import CallbackContext
from config import BINANCE_API_KEY, BINANCE_API_SECRET
from db import log_trade

client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)

    def trade(update: Update, context: CallbackContext):
        if len(context.args) < 3:
            update.message.reply_text("مثال: /trade BTCUSDT buy 0.001")
            return

        symbol = context.args[0].upper()
        side = context.args[1].lower()
        quantity = float(context.args[2])

        try:
            if side == 'buy':
                order = client.order_market_buy(symbol=symbol, quantity=quantity)
            elif side == 'sell':
                 order = client.order_market_sell(symbol=symbol, quantity=quantity)
            else:
                update.message.reply_text("يجب أن يكون side إما buy أو sell")
                return

            price = float(order['fills'][0]['price'])
            log_trade(symbol, side, quantity, price)

            update.message.reply_text(
                f"تم تنفيذ الصفقة: {side.upper()} {quantity} {symbol} بسعر {price}$"
            )
        except Exception as e:
            update.message.reply_text(f"حدث خطأ أثناء تنفيذ الصفقة: {e}")
