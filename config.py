import os

from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    DEBUG = os.getenv("DEBUG") == "True"

    DATABASE = os.path.join(
        "database",
        os.getenv("DATABASE_NAME")
    )

    LOG_FILE = "logs/app.log"