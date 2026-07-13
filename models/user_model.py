from database.db import get_connection


class User:

    @staticmethod
    def get_user(username):

        with get_connection() as connection:

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT *
                    FROM users
                    WHERE username=%s
                    """,
                    (username,)
                )

                return cursor.fetchone()