import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        symbol TEXT,
        side TEXT,
        quantity REAL,
        price REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()
    conn.close()

def log_trade(user_id, symbol, side, quantity, price):
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("INSERT INTO trades (user_id, symbol, side, quantity, price) VALUES (?, ?, ?, ?, ?)",
              (user_id, symbol, side, quantity, price))
    conn.commit()
    conn.close()