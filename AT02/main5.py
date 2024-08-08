import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER)
    ''')
    return conn

def add_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()

