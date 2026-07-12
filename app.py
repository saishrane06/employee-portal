from flask import Flask

from config import Config

from routes.auth import auth

from routes.employee import employee
import logging
import os

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = app.config["SECRET_KEY"]
app.register_blueprint(auth)
app.register_blueprint(employee)
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename=app.config["LOG_FILE"],
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config["DEBUG"]
    )