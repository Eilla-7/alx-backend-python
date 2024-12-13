#!/usr/bin/python3

"""lazy paginate module"""

import mysql.connector


DB_NAME = "ALX_prodev"
DB_USER = ""
DB_PASS = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306


def paginate_users(page_size, offset):
    """
    Fetch users with LIMIT and OFFSET for pagination.
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

        cursor.execute("SELECT * FROM user_data LIMIT %s OFFSET %s", (page_size, offset))

        for row in cursor:
            yield row

    except mysql.connector.Error as err:
        print(f"Database error: {err.msg}")
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


def lazy_paginate(page_size):
    """
    Generator that lazily fetches paginated data from the database using OFFSET.
    """
    offset = 0
    while True:
        users = list(paginate_users(page_size, offset))
        if not users:
            break
        yield users
        offset += page_size 
