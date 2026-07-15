import psycopg2
from psycopg2.extras import RealDictCursor
import logging  
from config import Config


def get_connection():

    logging.info(
        "Connecting to PostgreSQL..."
    )

    connection = psycopg2.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        database=Config.DB_NAME,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        cursor_factory=RealDictCursor
    )

    logging.info("Database connection successful.")

    return connection