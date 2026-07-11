from database.database import get_db_connection


class User:

    @staticmethod
    def get_user(username):

        connection = get_db_connection()

        cursor = connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE username = ?
            """,
            (username,)
        )

        user = cursor.fetchone()

        connection.close()

        return user