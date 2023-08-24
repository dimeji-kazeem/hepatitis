import sqlite3
import threading

sqlite_local = threading.local()

def get_connection():
    if not hasattr(sqlite_local, "connection"):
        sqlite_local.connection = sqlite3.connect("useDB.db")
    return sqlite_local.connection

# Functions
def create_usertable():
    connection = get_connection()
    c = connection.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)')
    connection.commit()
    c.close()

def add_user(username, password):
    connection = get_connection()
    c = connection.cursor()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    connection.commit()
    c.close()

def login_user(username, password):
    connection = get_connection()
    c = connection.cursor()
    c.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = c.fetchone()
    c.close()
    return user is not None

def view_all_users():
    connection = get_connection()
    c = connection.cursor()
    c.execute('SELECT username FROM users')
    all_users = c.fetchall()
    c.close()
    return all_users