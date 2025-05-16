from utils.databaseInfo import connectToDatabase
import mysql.connector

def getFTList(company_id):
    
    food_trucks = []
    query_food_trucks_list = "SELECT * FROM food_trucks WHERE company_id = %s"
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(query_food_trucks_list, (company_id,))
        food_trucks = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    
    finally:
        cursor.close()
        foodTruckDb.close()
    
    return food_trucks