import sqlite3
from werkzeug.security import generate_password_hash

connection = sqlite3.connect("database/employee.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

username TEXT UNIQUE NOT NULL,

password TEXT NOT NULL

)
""")

hashed_password = generate_password_hash("admin123")

cursor.execute("""
INSERT OR IGNORE INTO users(username,password)

VALUES(?,?)
""", ("admin", hashed_password))

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(

id INTEGER PRIMARY KEY AUTOINCREMENT,

employee_id TEXT UNIQUE NOT NULL,

first_name TEXT NOT NULL,

last_name TEXT NOT NULL,

email TEXT UNIQUE NOT NULL,

phone TEXT,

department TEXT,

designation TEXT,

salary REAL,

joining_date TEXT,

status TEXT DEFAULT 'Active'

)
""")

connection.commit()

connection.close()

print("Database Created Successfully")