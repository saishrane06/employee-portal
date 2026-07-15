from flask import Flask
from flask import render_template
from config import Config

from routes.auth import auth

from routes.employee import employee
from routes.health import health
import logging
import os
import sys

app = Flask(__name__)

app.config.from_object(Config)

Config.validate()

app.secret_key = app.config["SECRET_KEY"]
app.register_blueprint(auth)
app.register_blueprint(employee)
app.register_blueprint(health)

#os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("======================================")
logging.info("Employee Portal Starting...")
logging.info("Application initialized successfully")
logging.info("======================================")

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config["DEBUG"]
    )