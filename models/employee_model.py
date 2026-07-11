from database.database import get_db_connection


class Employee:

    @staticmethod
    def get_all():

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM employees
            ORDER BY employee_id
        """)

        employees = cursor.fetchall()

        connection.close()

        return employees


    @staticmethod
    def get_by_id(employee_id):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM employees
            WHERE id = ?
        """, (employee_id,))

        employee = cursor.fetchone()

        connection.close()

        return employee


    @staticmethod
    def add(
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
    ):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO employees(

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

            VALUES(?,?,?,?,?,?,?,?,?,?)

        """,(

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

        ))

        connection.commit()

        connection.close()


    @staticmethod
    def update(

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

    ):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""

            UPDATE employees

            SET

                first_name=?,

                last_name=?,

                email=?,

                phone=?,

                department=?,

                designation=?,

                salary=?,

                joining_date=?,

                status=?

            WHERE id=?

        """,(

            first_name,

            last_name,

            email,

            phone,

            department,

            designation,

            salary,

            joining_date,

            status,

            id

        ))

        connection.commit()

        connection.close()


    @staticmethod
    def delete(id):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""

            DELETE FROM employees

            WHERE id=?

        """,(id,))

        connection.commit()

        connection.close()

    @staticmethod
    def get_last_employee():

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT employee_id

            FROM employees

            ORDER BY id DESC

            LIMIT 1

        """)

        employee = cursor.fetchone()

        connection.close()

        return employee
    
    @staticmethod
    def email_exists(email):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute("""

            SELECT *

            FROM employees

            WHERE email=?

        """,(email,))

        employee = cursor.fetchone()

        connection.close()

        return employee