import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = os.getenv("DEBUG") == "True"
    DATABASE_NAME = os.getenv("DATABASE_NAME")