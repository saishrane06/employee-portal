from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

from werkzeug.security import check_password_hash

from models.user_model import User

auth = Blueprint("auth", __name__)


@auth.route("/")
def home():

    return render_template("index.html")


@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User.get_user(username)

        if user:

            if check_password_hash(
                user["password"],
                password
            ):

                session["user"] = username

                flash(
                    "Login Successful",
                    "success"
                )

                return redirect(
                    url_for("auth.dashboard")
                )

        flash(
            "Invalid Username or Password",
            "danger"
        )

    return render_template("login.html")


@auth.route("/dashboard")
def dashboard():

    if "user" not in session:

        flash(
            "Please login first",
            "warning"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@auth.route("/logout")
def logout():

    session.clear()

    flash(
        "Logged out successfully",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )