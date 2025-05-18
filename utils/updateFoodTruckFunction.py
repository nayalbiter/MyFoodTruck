from flask import request, redirect, url_for, flash
from utils.databaseInfo import connectToDatabase
import mysql.connector

def updateTruckInfo():
    food_truck_id =  request.form['food_truck_id']
    food_truck_name = request.form['foodTruckName']
    full_address = request.form['address']
    phone_number = request.form['phone']
    business_hours = request.form['hours']
    
    updateFoodTruckQuery = """
        update food_trucks
        set food_truck_name = %s,
            full_address = %s,
            phone_number = %s,
            business_hours = %s
        where food_truck_id = %s
    """
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(updateFoodTruckQuery, (food_truck_name, full_address,  phone_number, business_hours, food_truck_id ))
        foodTruckDb.commit()
        print("the food truck was updated successfully")
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    return redirect(url_for("go2CompanyMainPageAfterLogIn"))     
    