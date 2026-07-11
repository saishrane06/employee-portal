from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    url_for
)

from models.employee_model import Employee
from flask import request, flash
employee = Blueprint(
    "employee",
    __name__,
    url_prefix="/employees"
)

def generate_employee_id():

    employee = Employee.get_last_employee()

    if employee:

        last_id = int(employee["employee_id"][3:])

        return f"EMP{last_id + 1:03d}"

    return "EMP001"

@employee.route("/")
def employee_list():

    if "user" not in session:

        return redirect(url_for("auth.login"))

    employees = Employee.get_all()

    return render_template(
        "employees.html",
        employees=employees
    )

@employee.route("/add", methods=["GET","POST"])

def add_employee():

    if "user" not in session:

        return redirect(url_for("auth.login"))

    if request.method == "POST":

        employee_id = generate_employee_id()

        first_name = request.form["first_name"]

        last_name = request.form["last_name"]

        email = request.form["email"]

        phone = request.form["phone"]

        department = request.form["department"]

        designation = request.form["designation"]

        salary = request.form["salary"]

        joining_date = request.form["joining_date"]

        status = request.form["status"]

        if Employee.email_exists(email):

            flash(

                "Email already exists",

                "danger"

            )

            return redirect(

                url_for("employee.add_employee")

            )

        Employee.add(

            employee_id,

            first_name,

            last_name,

            email,

            phone,

            department,

            designation,

            salary,

            joining_date,

            status

        )

        flash(

            "Employee added successfully",

            "success"

        )

        return redirect(

            url_for("employee.employee_list")

        )

    return render_template(

        "add_employee.html"

    )

@employee.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_employee(id):

    if "user" not in session:
        return redirect(url_for("auth.login"))

    employee_data = Employee.get_by_id(id)

    if not employee_data:
        flash("Employee not found", "danger")
        return redirect(url_for("employee.employee_list"))

    if request.method == "POST":

        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        phone = request.form["phone"]
        department = request.form["department"]
        designation = request.form["designation"]
        salary = request.form["salary"]
        joining_date = request.form["joining_date"]
        status = request.form["status"]

        if Employee.email_exists_for_other(email, id):

            flash(
                "Email already exists",
                "danger"
            )

            return redirect(
                url_for(
                    "employee.edit_employee",
                    id=id
                )
            )

        Employee.update(

            id,

            first_name,

            last_name,

            email,

            phone,

            department,

            designation,

            salary,

            joining_date,

            status

        )

        flash(
            "Employee updated successfully",
            "success"
        )

        return redirect(
            url_for("employee.employee_list")
        )

    return render_template(
        "edit_employee.html",
        employee=employee_data
    )