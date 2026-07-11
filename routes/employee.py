from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for
)

from models.employee_model import Employee

employee = Blueprint(
    "employee",
    __name__,
    url_prefix="/employees"
)


@employee.route("/")
def employee_list():

    if "user" not in session:

        return redirect(url_for("auth.login"))

    employees = Employee.get_all()

    return render_template(
        "employees.html",
        employees=employees
    )