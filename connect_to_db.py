import sqlite3


def create_connection():
    connection = sqlite3.connect("data.db")
    return connection


def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
 CREATE TABLE IF NOT EXISTS todolist (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 title TEXT NOT NULL)
 """)
    connection.commit()
    connection.close()


create_table()
