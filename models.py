import sqlite3

def create_table():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def insert_test_user():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", ("test@example.com",))
    data = cursor.fetchall()

    if not data:  # Only insert the test user if they don't exist yet
        cursor.execute('''
            INSERT INTO users (email, password)
            VALUES (?, ?)
        ''', ("test@example.com", "password"))
        conn.commit()

    conn.close()

def check_credentials(email, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    data = cursor.fetchall()
    conn.close()

    return bool(data)
