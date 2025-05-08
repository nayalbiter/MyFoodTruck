from flask import Flask, redirect, render_template, request, url_for
from utils.databaseInfo import connectToDatabase
import mysql.connector

def insertNewFoodTruck():
    company_id = request.form['company_id']
    food_truck_name = request.form['foodTruckName']
    full_address = request.form['address']
    phone_number = request.form['phone']
    business_hours = request.form['hours']
    
    
    insertFoodTruckQuery = """
    INSERT INTO food_trucks (food_truck_name, full_address, phone_number, business_hours, company_id )
    VALUES (%s, %s, %s, %s, %s)
    """
    try:
        foodTruckDb = connectToDatabase()
        cursor = foodTruckDb.cursor(dictionary=True)
        cursor.execute(insertFoodTruckQuery, (food_truck_name, full_address, phone_number, business_hours, company_id))
        foodTruckDb.commit()
        
        cursor.execute("SELECT * FROM food_companies WHERE company_id = %s", (company_id,))
        company = cursor.fetchone()

        cursor.execute("SELECT * FROM food_trucks WHERE company_id = %s", (company_id,))
        food_trucks = cursor.fetchall()
    
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return f"An error happened while processing your request: {err}"
    
    finally:
        cursor.close()
        foodTruckDb.close()
        
    return render_template("foodCompanyPage.html", company=company, food_trucks=food_trucks)

