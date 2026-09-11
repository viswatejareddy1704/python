import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='viswa1704',
        database='bookmyshow'
    )

    if connection.is_connected():
        print("Successfully connected to MySQL database....")

        cursor = connection.cursor()

        print("All table names in MySQL database:")

        cursor.execute("SHOW TABLES;")

        record = cursor.fetchone()

        print("One table name:", record)

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed.")