import sqlite3

def init_db():
    conn = sqlite3.connect('security_app.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE,
                 password TEXT
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS ddos_history (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 src TEXT, dst TEXT, length INTEGER, timestamp TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS traffic_logs (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 src TEXT, dst TEXT, length INTEGER, timestamp TEXT)''')
    conn.commit()
    conn.close()

def save_ddos_event(event):
    conn = sqlite3.connect('security_app.db')
    c = conn.cursor()
    c.execute("INSERT INTO ddos_history (src, dst, length, timestamp) VALUES (?, ?, ?, ?)",
              (event['src'], event['dst'], event['length'], str(event['timestamp'])))
    conn.commit()
    conn.close()

def save_traffic_log(log):
    conn = sqlite3.connect('security_app.db')
    c = conn.cursor()
    c.execute("INSERT INTO traffic_logs (src, dst, length, timestamp) VALUES (?, ?, ?, ?)",
              (log['src'], log['dst'], log['length'], str(log['timestamp'])))
    conn.commit()
    conn.close()
