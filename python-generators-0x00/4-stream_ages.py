import mysql.connector


DB_NAME = "ALX_prodev"
DB_USER = ""
DB_PASS = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306


def stream_user_ages():
    """
    Generator function that lazily streams user ages one by one from the database.
    """
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

        cursor.execute("SELECT age FROM user_data")

        for row in cursor:
            yield row['age']

    except mysql.connector.Error as err:
        print(f"Database error: {err.msg}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def compute_average_age():
    """
    Compute the average age of users using the lazy generator without loading all data into memory.
    """
    total_age = 0
    user_count = 0

    for age in stream_user_ages():
        total_age += int(age)
        user_count += 1

    average_age = total_age / user_count if user_count > 0 else 0
    return average_age
