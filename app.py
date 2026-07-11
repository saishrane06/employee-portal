from flask import Flask

from config import Config

from routes.auth import auth

from routes.employee import employee

app = Flask(__name__)

app.config.from_object(Config)
app.secret_key = app.config["SECRET_KEY"]
app.register_blueprint(auth)

app.register_blueprint(employee)

if __name__=="__main__":

    app.run(debug=app.config["DEBUG"])