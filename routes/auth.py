import sqlite3

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for,
    current_app
)

auth = Blueprint("auth",__name__)


@auth.route("/")
def home():

    return render_template("index.html")


@auth.route("/login",methods=["GET","POST"])
def login():

    if request.method=="POST":

        username=request.form["username"]

        password=request.form["password"]

        connection=sqlite3.connect(
            current_app.config["DATABASE"]
        )

        cursor=connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username=?
            AND password=?
            """,
            (username,password)
        )

        user=cursor.fetchone()

        connection.close()

        if user:

            session["user"]=username

            return redirect(url_for("auth.dashboard"))

        return render_template(
            "login.html",
            error="Invalid Username or Password"
        )

    return render_template("login.html")


@auth.route("/dashboard")
def dashboard():

    if "user" not in session:

        return redirect(url_for("auth.login"))

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("auth.login"))