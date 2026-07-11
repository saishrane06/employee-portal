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

connection.commit()

connection.close()

print("Database Created Successfully")