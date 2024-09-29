import sqlite3
from datetime import datetime

DB_FILE = 'patient_data.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS heart_rate_data
                      (timestamp TEXT, heart_rate INTEGER)''')
    conn.commit()
    conn.close()

def insert_heart_rate(heart_rate):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute("INSERT INTO heart_rate_data (timestamp, heart_rate) VALUES (?, ?)", (timestamp, heart_rate))
    conn.commit()
    conn.close()

def get_historical_data():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM heart_rate_data")
    data = cursor.fetchall()
    conn.close()
    return data