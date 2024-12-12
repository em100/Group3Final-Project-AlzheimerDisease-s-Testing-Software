import mysql.connector
from mysql.connector import Error

# database.py
class Database:
    @staticmethod
    def connect_db():
        """
        Establishes a connection to the MySQL database.

        Returns:
            connection (mysql.connector.connection.MySQLConnection): 
                The connection object if the connection is successful.
            None: 
                If the connection fails.
        """
        try:
            # Attempt to connect to the MySQL database
            connection = mysql.connector.connect(
                host='localhost',
                database='alzheimer_testing',
                user='root',
                password='emus100M!'
            )
            # Check if the connection is established
            if connection.is_connected():
                return connection
        except Error as e:
            # Print the error if connection fails
            print("Error while connecting to MySQL", e)
        # Return None if connection is not established
        return None