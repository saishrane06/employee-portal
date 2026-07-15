import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    DEBUG = os.getenv("DEBUG", "False") == "True"

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    LOG_FILE = os.path.join(
        BASE_DIR,
        "logs",
        "app.log"
    )

    @classmethod
    def validate(cls):

        required = {
            "SECRET_KEY": cls.SECRET_KEY,
            "DB_HOST": cls.DB_HOST,
            "DB_PORT": cls.DB_PORT,
            "DB_NAME": cls.DB_NAME,
            "DB_USER": cls.DB_USER,
            "DB_PASSWORD": cls.DB_PASSWORD,
        }

        missing = []

        for key, value in required.items():
            if not value:
                missing.append(key)

        if missing:
            raise ValueError(
                f"Missing environment variables: {', '.join(missing)}"
            )