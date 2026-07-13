from werkzeug.security import generate_password_hash
from database.db import get_connection

username = "admin"
password = "Admin@123"   # Change later if you like

hashed_password = generate_password_hash(password)

with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (%s, %s)
            """,
            (username, hashed_password)
        )

print("✅ Admin user created successfully!")