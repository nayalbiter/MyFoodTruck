from flask import Flask, render_template, request
from utils.databaseInfo import connectToDatabase
import mysql.connector

def addNewFoodTruck():
    food_truck_name = request.form['foodTruckName']
    food_truck_location = request.form['address']
    phone_number = request.form['phone']
    business_hours = request.form['hours']
    
    #fix this to add the foreign key here-----------------------------------------------------------
    insertFoodTruckQuery = """
    INSERT INTO food_trucks (food_truck_name, food_truck_location, phone_number, business_hours)
    VALUES (%s, %s, %s, %s)
    """
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(insertFoodTruckQuery, (food_truck_name, food_truck_location, phone_number, business_hours))
        foodTruckDb.commit()

        #show the information of the company in the food Company main page
        cursor.execute("""
            SELECT company_name, food_description, business_website, email 
            FROM food_companies 
            WHERE company_Id = LAST_INSERT_ID()
        """)
        company = cursor.fetchone()
        
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}", 500  #server error
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    print(f"Company details fetched: {company}")
    return render_template("foodCompanyPage.html", company=company)