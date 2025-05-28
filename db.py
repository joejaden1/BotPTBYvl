import sqlite3

def init_db():
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT,
        side TEXT,
        quantity REAL,
        price REAL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
    conn.commit()
    conn.close()

def log_trade(symbol, side, quantity, price):
    conn = sqlite3.connect("bot.db")
    c = conn.cursor()
    c.execute("INSERT INTO trades (symbol, side, quantity, price) VALUES (?, ?, ?, ?)",
    (symbol, side, quantity, price))
    conn.commit()
    conn.close()
