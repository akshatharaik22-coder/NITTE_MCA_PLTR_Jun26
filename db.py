import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akshatha123@#",
        database="hostel_db"
    )
