import sqlite3
import pandas as pd

def fetch_ddos_history():
    conn = sqlite3.connect('security_app.db')
    df = pd.read_sql_query("SELECT * FROM ddos_history", conn)
    conn.close()
    return df

def fetch_traffic_logs():
    conn = sqlite3.connect('security_app.db')
    df = pd.read_sql_query("SELECT * FROM traffic_logs", conn)
    conn.close()
    return df
