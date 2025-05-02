import mysql.connector

#connect to database locally CHECK
def connectToDatabase():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Food_Trucks_Database"
    )