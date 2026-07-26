import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("test.db", check_same_thread=False) # Establish a connection to the SQLite database (test.db). The check_same_thread=False parameter allows the connection to be shared across multiple threads, which is useful in a web application context.

cursor = conn.cursor() # Create a cursor object to interact with the database

# Create a table if it doesn't exist
cursor.execute("""
 CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL)
""")

conn.commit() # Commit the changes to the database

@app.get('/')
def home():
    return {
        "message": "SQLite database connection established successfully!"
    }