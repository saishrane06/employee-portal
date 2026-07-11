from flask import Flask

from config import Config

from routes import auth
from routes import employee

app = Flask(__name__)

app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(auth)

app.register_blueprint(employee)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])