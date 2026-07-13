from database.db import get_connection


class Employee:

    @staticmethod
    def get_all():

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT *
                    FROM employees
                    ORDER BY employee_id
                """)

                return cursor.fetchall()

    @staticmethod
    def get_by_id(employee_id):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""
                    SELECT *
                    FROM employees
                    WHERE id=%s
                """, (employee_id,))

                return cursor.fetchone()

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

        with get_connection() as connection:

            with connection.cursor() as cursor:

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

                    VALUES(
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s
                    )
                """, (

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

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    UPDATE employees

                    SET

                        first_name=%s,
                        last_name=%s,
                        email=%s,
                        phone=%s,
                        department=%s,
                        designation=%s,
                        salary=%s,
                        joining_date=%s,
                        status=%s

                    WHERE id=%s

                """, (

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

    @staticmethod
    def delete(id):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    DELETE
                    FROM employees
                    WHERE id=%s

                """, (id,))

    @staticmethod
    def get_last_employee():

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    SELECT employee_id

                    FROM employees

                    ORDER BY id DESC

                    LIMIT 1

                """)

                return cursor.fetchone()

    @staticmethod
    def email_exists(email):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    SELECT *

                    FROM employees

                    WHERE email=%s

                """, (email,))

                return cursor.fetchone()

    @staticmethod
    def email_exists_for_other(email, employee_id):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    SELECT *

                    FROM employees

                    WHERE email=%s

                    AND id!=%s

                """, (

                    email,
                    employee_id

                ))

                return cursor.fetchone()

    @staticmethod
    def search(search_term):

        query = f"%{search_term}%"

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute("""

                    SELECT *

                    FROM employees

                    WHERE employee_id ILIKE %s
                    OR first_name ILIKE %s
                    OR last_name ILIKE %s
                    OR email ILIKE %s
                    OR department ILIKE %s
                    OR designation ILIKE %s

                    ORDER BY employee_id

                """, (

                    query,
                    query,
                    query,
                    query,
                    query,
                    query

                ))

                return cursor.fetchall()