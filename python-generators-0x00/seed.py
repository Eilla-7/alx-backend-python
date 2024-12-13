#!/usr/bin/python3

"""
Getting started with python generators
"""

import mysql.connector
import csv

DB_NAME = "ALX_prodev"
DB_USER = "root"
DB_PASS = "root"


def connect_db():
    """connects to the mysql database server"""

    connect = mysql.connector.connect(
        user=DB_USER,
        password=DB_PASS,
        host='127.0.0.1',
        port=3306,
    )

    return connect


def create_database(connection):
    """creates the database ALX_prodev if it does not exist"""
    cur = connection.cursor()
    try:
        cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except mysql.connector.Error as err:
        print(f"Failed: {err.msg}")
    cur.close()


def connect_to_prodev():
    """connects the the ALX_prodev database in MYSQL"""
    try:
        connect = mysql.connector.connect(
            user=f"{DB_USER}", password=f"{DB_PASS}", database=f"{DB_NAME}"
        )
    except mysql.connector.Error as err:
        print(f"Failed: {err.msg}")

    return connect


def create_table(connection):
    """
    creates a table user_data (if it does not exists)
    with the required fields
    """
    cur = connection.cursor()
    user_data = """CREATE TABLE IF NOT EXISTS user_data (
        user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL(3, 0) NOT NULL
    )"""

    try:
        cur.execute(user_data)
    except mysql.connector.Error as err:
        print(err.msg)


def insert_data(connection, data):
    """inserts data in the database if it does not exist"""
    cur = connection.cursor()

    try:
        with open(data, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                email = row["email"]
                age = row["age"]

                try:
                    cur.execute(
                        """
                        INSERT INTO user_data (name, email, age)
                        VALUES (%s, %s, %s)
                        """,
                        (name, email, age),
                    )
                except mysql.connector.Error as err:
                    print(f"Failed to insert row {row}: {err.msg}")
            connection.commit()
    except FileNotFoundError:
        print(f"File {data} not found.")
    except Exception as err:
        print(f"Unexpected error: {err}")
    finally:
        cur.close()
