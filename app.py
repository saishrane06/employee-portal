from flask import Flask, render_template
from config import Config

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])