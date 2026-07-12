import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "dev-secret-key"
    )

    DEBUG = os.getenv(
        "DEBUG",
        "False"
    ) == "True"

    DATABASE_NAME = os.getenv(
        "DATABASE_NAME",
        "employee.db"
    )

    DATABASE = os.path.join(
        BASE_DIR,
        "database",
        DATABASE_NAME
    )

    LOG_FILE = os.path.join(
        BASE_DIR,
        "logs",
        "app.log"
    )