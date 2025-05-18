from utils.databaseInfo import connectToDatabase
import mysql.connector

def getFoodTruckDetails(food_truck_id):
    
    food_truck_info = None
    foodTruckQuery = "select * from food_trucks where food_truck_id = %s"
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(foodTruckQuery, (food_truck_id,))
        food_truck_info = cursor.fetchone()
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    
    finally:
        cursor.close()
        foodTruckDb.close()
    
    return food_truck_info