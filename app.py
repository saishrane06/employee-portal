from flask import Flask, render_template
from config import Config
from routes.auth import auth
from routes.employee import employee
from routes.health import health
import logging
import sys


def create_app():

    app = Flask(__name__)

    # Load configuration based on FLASK_CONFIG
    app.config.from_object(Config)

    app.secret_key = app.config["SECRET_KEY"]

    # Register Blueprints
    app.register_blueprint(auth)
    app.register_blueprint(employee)
    app.register_blueprint(health)

    # Configure Logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Error Handlers
    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_error(error):
        return render_template("500.html"), 500

    return app


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=app.config["DEBUG"]
    )