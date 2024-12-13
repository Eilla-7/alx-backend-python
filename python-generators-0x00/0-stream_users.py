import mysql.connector

# Database connection details
DB_NAME = "ALX_prodev"
DB_USER = "root"
DB_PASS = "Elolo2238~"
DB_HOST = "127.0.0.1"
DB_PORT = 3306


def stream_users():
    """Generator function to stream rows from user_data table one by one."""
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM user_data")

        for row in cursor:
            yield row

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Database error: {err.msg}")
