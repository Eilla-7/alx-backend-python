#!/usr/bin/python3

"""batch processing module"""

import mysql.connector


# Database connection details
DB_NAME = "ALX_prodev"
DB_USER = ""
DB_PASS = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306


def stream_users_in_batches(batch_size):
    """
    Generator function to fetch rows from the database in batches.
    Yields batches of users from the database of size 'batch_size'.
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

        cursor.execute("SELECT * FROM user_data")

        batch = []
        for row in cursor:
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        
        if batch:
            yield batch

    except mysql.connector.Error as err:
        print(f"Database error: {err.msg}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def batch_processing(batch_size):
    """
    Processes each batch using the stream_users_in_batches generator.
    Filters users over the age of 25 from each batch.
    """
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user.get("age") and user["age"] > 25]
        print(f"Processing Batch: Found {len(filtered_users)} users over age 25")
        for user in filtered_users:
            print(user)
