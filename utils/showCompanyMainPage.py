from flask import render_template
from flask_login import current_user
from utils.databaseInfo import connectToDatabase
import mysql.connector

def getCompanyMainPage():
    print("Authenticated?", current_user.is_authenticated)
    print("Company email:", current_user.company_email)
    
    company_id = current_user.id
    
    query_food_trucks_list = "SELECT * FROM food_trucks WHERE company_id = %s"
    
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(query_food_trucks_list, (company_id,))
        food_trucks = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}"
    
    finally:
        cursor.close()
        foodTruckDb.close()
    
    return render_template("foodCompanyPage.html", company = current_user, food_trucks = food_trucks )